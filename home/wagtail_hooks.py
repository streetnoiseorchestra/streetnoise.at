from home.models import BandFriend
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet


class BandFriendViewSet(SnippetViewSet):
    model = BandFriend
    icon = "suitcase"
    menu_label = "Band Friends"
    add_to_admin_menu = True


register_snippet(BandFriendViewSet)
