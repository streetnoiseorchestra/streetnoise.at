from home.models import BandFriend
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register


@modeladmin_register
class BandFriendAdmin(ModelAdmin):
    menu_label = "Band Friends"
    menu_icon = "suitcase"  # change as required
    model = BandFriend
