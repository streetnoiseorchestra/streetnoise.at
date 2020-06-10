import hashlib
import json
import logging
from hmac import compare_digest

import requests

from django.conf import settings
from django.utils.translation import gettext as _
from django.utils.http import urlencode

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
    confirm_code = sign_confirmation_code(email, settings.SECRET_KEY)
    confirm_params = urlencode({"subscriber_email": email, "code": confirm_code})
    withdraw_params = urlencode({"subscriber_email": email, "confirm": "yes"})
    confirm_url = f"{confirm_url_base}?{confirm_params}"
    withdraw_url = f"{withdraw_url_base}?{withdraw_params}"

    member = {
        "address": email,
        "name": name,
        "vars": json.dumps(
            {
                "first_optin_at": consented_at,
                "double_optin_at": None,
                "consented_from": consented_from,
            }
        ),
        "subscribed": "no",
    }
    r = update_list_member(member)
    if r.status_code != 200:
        logger.error(
            "mailgun add user to list (1st time) failed: {}".format(r.status_code)
        )
        return False

    r = send_double_optin_email(name, email, confirm_url, withdraw_url)
    if r.status_code != 200:
        logger.error("mailgun double optin send failed: {}".format(r.status_code))

    return r.status_code == 200


def second_opt_in(code, email, double_optin_at):
    if not validate_confirmation_code(code, email, settings.SECRET_KEY):
        logger.error("Invalid second opt in code")
        return False
    member = get_list_member(email)
    if not member:
        logger.error("mailgun list member not found")
        return False
    vars = member["vars"]
    vars["double_optin_at"] = double_optin_at
    member["subscribed"] = "yes"
    member["vars"] = json.dumps(vars)
    r = update_list_member(member)
    if r.status_code != 200:
        logger.error(
            "mailgun add user to list (2nd time) failed: {}".format(r.status_code)
        )

    return r.status_code == 200


def mailgun_unsubscribe(email, consent_withdrawn_at):
    member = get_list_member(email)
    if not member:
        logger.error("mailgun list member not found")
        return 404

    vars = member["vars"]
    vars["consent_withdrawn_at"] = consent_withdrawn_at
    member["subscribed"] = "no"
    member["vars"] = json.dumps(vars)
    r = update_list_member(member)
    if r.status_code != 200:
        logger.error("mailgun unsubscribe failed: {}".format(r.status_code))

    return r.status_code == 200


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
