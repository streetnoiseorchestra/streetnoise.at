from allauth.account.adapter import DefaultAccountAdapter

class SNOAccountAdapter(DefaultAccountAdapter):
    """
    https://django-allauth.readthedocs.io/en/latest/advanced.html#custom-redirects """

    def is_open_for_signup(self, request):
        return False
