import logging

from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.models import EmailAddress
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

logger = logging.getLogger(__name__)


class SNOAccountAdapter(DefaultAccountAdapter):
    """https://django-allauth.readthedocs.io/en/latest/advanced.html#creating-and-populating-user-instances"""

    def is_open_for_signup(self, request):
        return False


class SNOSocialAccountAdapter(DefaultSocialAccountAdapter):
    """https://django-allauth.readthedocs.io/en/latest/advanced.html#creating-and-populating-user-instances"""

    def is_auto_signup_allowed(self, request, sociallogin):
        return True

    def is_open_for_signup(self, request, socialaccount):
        return True

    def pre_social_login(self, request, sociallogin):
        # social account already exists, so this is just a login
        if sociallogin.is_existing:
            return

        # some social logins don't have an email address
        if not sociallogin.email_addresses:
            return

        # find the first verified email that we get from this sociallogin
        verified_email = None
        for email in sociallogin.email_addresses:
            if email.verified:
                verified_email = email
                break

        # no verified emails found, nothing more to do
        if not verified_email:
            return

        # check if given email address already exists as a verified email on
        # an existing user's account
        try:
            existing_email = EmailAddress.objects.get(email__iexact=email.email, verified=True)
        except EmailAddress.DoesNotExist:
            return

        logger.info(f"connecting {existing_email}")
        # if it does, connect this new social login to the existing user
        sociallogin.connect(request, existing_email.user)
