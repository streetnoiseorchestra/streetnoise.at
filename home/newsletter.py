import hashlib
import hmac
import json
import logging
from hmac import compare_digest
from datetime import datetime

import requests

from django.conf import settings
from django.utils.translation import gettext as _
from django.utils.http import urlencode
from django.http import HttpResponse, JsonResponse

from newsletter.models import NewsletterSubscriber

logger = logging.getLogger(__name__)


def sign_confirmation_code(value, secret):
    m = hashlib.sha256()
    m.update(value.encode("utf-8"))
    m.update(secret.encode("utf-8"))
    return m.hexdigest()


def validate_confirmation_code(user_code, email, secret):
    good_code = sign_confirmation_code(email, secret)
    return compare_digest(good_code.encode("utf-8"), user_code.encode("utf-8"))


def first_opt_in(
    name, email, consented_at, consented_from, confirm_url_base, withdraw_url_base
):

    NewsletterSubscriber.objects.get_or_create(
        email=email,
        name=name,
        first_optin_at=consented_at,
        consented_from=consented_from,
        subscribed=False,
    )

    confirm_code = sign_confirmation_code(email, settings.SECRET_KEY)
    confirm_params = urlencode({"subscriber_email": email, "code": confirm_code})
    withdraw_params = urlencode({"subscriber_email": email, "confirm": "yes"})
    confirm_url = f"{confirm_url_base}?{confirm_params}"
    withdraw_url = f"{withdraw_url_base}?{withdraw_params}"

    r = send_double_optin_email(name, email, confirm_url, withdraw_url)
    if r.status_code != 200:
        logger.error("mailgun double optin send failed: {}".format(r.status_code))

    return r.status_code == 200


def second_opt_in(code, email, double_optin_at):
    if not validate_confirmation_code(code, email, settings.SECRET_KEY):
        logger.error("Invalid second opt in code")
        return False

    try:
        subscriber = NewsletterSubscriber.objects.get(email=email)
    except NewsletterSubscriber.DoesNotExist:
        logger.error("cannot find NewsletterSubscriber for email")
        return False

    subscriber.double_optin_at = double_optin_at
    subscriber.bounce_score = 0
    subscriber.subscribed = True
    subscriber.consent_withdrawn_at = None
    subscriber.save()
    return True


def mailgun_unsubscribe(email, consent_withdrawn_at):

    try:
        subscriber = NewsletterSubscriber.objects.get(email=email)
    except NewsletterSubscriber.DoesNotExist:
        logger.error("cannot find NewsletterSubscriber for email")
        return 404

    subscriber.consent_withdrawn_at = consent_withdrawn_at
    subscriber.subscribed = False
    subscriber.save()
    return True


def send_double_optin_email(name, email, confirm_url, withdraw_url):
    payload = {
        "confirm_title": _(
            "Confirm to receive StreetNoise Orchestra announcements and updates."
        ),
        "confirm_msg": _(
            "We take privacy seriously, we'll only use your information to send you an update every so often. You can always contact us at orchestra@streetnoise.at"
        ),
        "withdraw_msg": _("You can withdraw your consent at anytime: "),
        "withdraw_link_text": _("unsubscribe"),
        "withdraw_link_url": withdraw_url,
        "confirm_button_url": confirm_url,
        "confirm_button_text": _("Yes, I confirm"),
    }
    subject = _("Can StreetNoise Orchestra send you emails?")
    to = f"{name} <{email}>"
    return requests.post(
        "https://api.eu.mailgun.net/v3/mg.streetnoise.at/messages",
        auth=("api", settings.MAILGUN_KEY),
        data={
            "from": settings.MAILGUN_NEWSLETTER_FROM,
            "to": to,
            "subject": subject,
            "template": "sno-newsletter-double-optin",
            "h:X-Mailgun-Variables": json.dumps(payload),
        },
    )


def get_list_member(email):
    r = requests.get(
        f"https://api.eu.mailgun.net/v3/lists/{settings.MAILGUN_NEWSLETTER_LIST}/members/{email}",
        auth=("api", settings.MAILGUN_KEY),
    )
    if r.status_code != 200:
        return False
    return r.json()["member"]


def update_list_member(member):
    member["upsert"] = "yes"
    return requests.post(
        f"https://api.eu.mailgun.net/v3/lists/{settings.MAILGUN_NEWSLETTER_LIST}/members",
        auth=("api", settings.MAILGUN_KEY),
        data=member,
    )


def valid_mailgun_signature(api_key, token, timestamp, signature):
    real_hash = hmac.new(
        key=api_key, msg=f"{timestamp}{token}", digestmod=hashlib.sha256()
    ).hexdigest()
    return signature == real_hash


def mailgun_handle_bounce(params):
    signature = params["signature"]
    if not valid_mailgun_signature(
        signature["token"], signature["timestamp"], signature["signature"]
    ):
        return HttpResponse(401)

    data = params["event-data"]
    error_code = params["delivery-status"]["code"]
    message_id = params["message"]["headers"]["message-id"]
    to_address = params["recipient"]
    severity = data["severity"]

    if data["event"] == "failed":
        if severity == "temporary":
            process_bounce(message_id, to_address, "soft", error_code)
        elif severity == "permanent":
            process_bounce(message_id, to_address, "hard", error_code)

    return HttpResponse(200)


# Bounce score added to the user when a temporary bounce happens.
SOFT_BOUNCE_SCORE = 1
# Bounce score added to the user when a permanent bounce happens.
HARD_BOUNCE_SCORE = 2
# Max bounce score before we will stop emailing a user.
BOUNCE_SCORE_THRESHOLD = 4
# Automatically reset bounce score after X days.
RESET_BOUNCE_AFTER_DAYS = 30


def process_bounce(message_id, to_address, bounce_score, error_code):
    if message_id is None or message_id == "":
        return
    if to_address is None or to_address == "":
        return

    try:
        subscriber = NewsletterSubscriber.objects.get(email=to_address)
    except NewsletterSubscriber.DoesNotExist:
        logger.error("cannot find NewsletterSubscriber for email")
        return

    old_score = subscriber.bounce_score
    new_score = subscriber.bounce_score + bounce_score
    subscriber.bounce_score = new_score
    subscriber.reset_bounce_score_on = datetime.utcnow() + datetime.timedelta(
        days=RESET_BOUNCE_AFTER_DAYS
    )

    if new_score >= RESET_BOUNCE_AFTER_DAYS:
        subscriber.subscribed = False

    subscriber.save()
