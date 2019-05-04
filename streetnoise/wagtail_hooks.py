from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from home.models import BandFriend


class BandFriendAdmin(ModelAdmin):
    model = BandFriend
