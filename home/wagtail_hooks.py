from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from home.models import BandFriend


class BandFriendAdmin(ModelAdmin):
    menu_label = "Band Friends"
    menu_icon = "fa-suitcase"  # change as required
    model = BandFriend


modeladmin_register(BandFriendAdmin)
