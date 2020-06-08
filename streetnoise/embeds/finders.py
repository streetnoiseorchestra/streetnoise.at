import re

from django.utils.translation import gettext_lazy as _

from wagtail.embeds.finders.base import EmbedFinder

# class AudioFinder(EmbedFinder):
class AudioFinder(EmbedFinder):
    def __init__(self, **options):
        exts = options["extensions"]
        self.mimetype = options["mimetype"]
        self.extension = exts
        self.fail_msg = _("Your browser cannot play audio files")
        self.patterns = []
        for ext in exts:
            self.patterns.append(re.compile(f".*\.{ext}$"))
        pass

    def accept(self, url):
        """
        Returns True if this finder knows how to fetch an embed for the URL.

        This should not have any side effects (no requests to external servers)
        """

        for pattern in self.patterns:
            if re.match(pattern, url):
                return True
        return False

    def find_embed(self, url, max_width=None):
        """
        Takes a URL and max width and returns a dictionary of information about the
        content to be used for embedding it on the site.

        This is the part that may make requests to external APIs.
        """
        mime = self.mimetype
        msg = "{} ({})".format(self.fail_msg, mime)
        return {
            "provider_name": "audio",
            "type": "rich",
            "width": 0,
            "height": 0,
            "html": f"""
                    <audio class="mejs__player"  style="width:100%;height:100%;">
                        <source src="{url}" type="{mime}">{msg}</audio>
            """,
        }
