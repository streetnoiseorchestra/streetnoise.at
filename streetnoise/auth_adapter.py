from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class SNOAccountAdapter(DefaultAccountAdapter):
    """https://django-allauth.readthedocs.io/en/latest/advanced.html#creating-and-populating-user-instances """

    def is_open_for_signup(self, request):
        return False

class SNOSocialAccountAdapter(DefaultSocialAccountAdapter):
    """https://django-allauth.readthedocs.io/en/latest/advanced.html#creating-and-populating-user-instances """

    def is_open_for_signup(self, request, socialaccount):
        return True
