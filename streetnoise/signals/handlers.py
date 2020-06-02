from django.dispatch import receiver
from django.contrib.auth.models import Group
from allauth.account.signals import user_signed_up

@receiver(user_signed_up)
def new_user_signup(sender, **kwargs):
    user = kwargs['user']
    g1 = Group.objects.get(name='Editors')
    user.groups.add(g1)
    user.save()
