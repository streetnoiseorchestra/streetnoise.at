from allauth.account.signals import user_signed_up
from django.contrib.auth.models import Group
from django.dispatch import receiver


@receiver(user_signed_up)
def new_user_signup(sender, **kwargs):
    user = kwargs["user"]
    g1 = Group.objects.get(name="Editors")
    user.groups.add(g1)
    g2 = Group.objects.get(name="Moderators")
    user.groups.add(g2)
    user.is_staff = True
    user.save()
