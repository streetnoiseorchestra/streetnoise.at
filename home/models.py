import uuid
from datetime import date

from blog.models import BlogIndexPage, BlogPage
from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from home.blocks import (
    ButtonBlock,
    FooterCTABlock,
    ImageGridBlock,
    ImageTileBlock,
    ImageTileBlock2,
    InfoItemBlock,
    MerchItemBlock,
    NewsletterSignupBlock,
    ParagraphImageBlock,
    TimelineHeaderBlock,
    TimelineItemBlock,
)
from modelcluster.fields import ParentalKey
from streetnoise.models import Page
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.embeds.blocks import EmbedBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import FieldPanel
from wagtail.models import Orderable, Site
from wagtail.snippets.models import register_snippet


@register_snippet
class BandFriend(models.Model):
    """
    A Django model to define the bread type
    It uses the `@register_snippet` decorator to allow it to be accessible
    via the Snippets UI. In the BreadPage model you'll see we use a ForeignKey
    to create the relationship between BreadType and BreadPage. This allows a
    single relationship (e.g only one BreadType can be added) that is one-way
    (e.g. BreadType will have no way to access related BreadPage objects)
    """

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    square_logo = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Square logo image; between 128px and 1000px",
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("location"),
                FieldPanel("website"),
                FieldPanel("facebook"),
                FieldPanel("square_logo"),
            ]
        )
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Band friends"


class HomePageBandFriend(Orderable, BandFriend):
    homepage = ParentalKey("FestivalPage", related_name="festival_bands", on_delete=models.CASCADE)

    band_friend = models.ForeignKey("home.BandFriend", on_delete=models.CASCADE, related_name="band_friends")
    panels = [
        FieldPanel("band_friend"),
    ]


class HomePage2(Page):
    menu_festival = models.CharField(max_length=100, blank=True)
    menu_who_we_are = models.CharField(max_length=100, blank=True)
    menu_upcoming_gigs = models.CharField(max_length=100, blank=True)
    menu_merch = models.CharField(max_length=100, blank=True)
    menu_join_us = models.CharField(max_length=100, blank=True)
    menu_request_gig = models.CharField(max_length=100, blank=True)
    menu_contact = models.CharField(max_length=100, blank=True)
    about_text = RichTextField(blank=True, features=["bold", "italic", "link"], verbose_name="About SNO")
    whoweare_title = models.CharField(max_length=100, blank=True, verbose_name="Who We Are title")
    whoweare_text = RichTextField(blank=True, features=["bold", "italic", "link"], verbose_name="Who We Are text")
    whoweare_gallery = StreamField(
        [
            ("image", ImageChooserBlock(label="Gallery Image")),
        ],
        null=True,
        blank=True,
        verbose_name="Who We Are Gallery",
    )

    gigs_title = models.CharField(max_length=100, blank=True)
    gigs_subtitle = models.CharField(max_length=100, blank=True)

    merch_title = models.CharField(max_length=100, blank=True)
    merch_subtitle = models.CharField(max_length=100, blank=True)
    merch_text = RichTextField(blank=True, features=["bold", "italic", "link"], verbose_name="Merch Detail")
    merch_items = StreamField(
        [
            ("merch", MerchItemBlock(label="Merch Item")),
        ],
        null=True,
        blank=True,
        verbose_name="Merchandise",
    )

    donate_title = models.CharField(max_length=100, blank=True)
    donate_online = models.CharField(max_length=100, blank=True)
    donate_offline = models.CharField(max_length=100, blank=True)
    donate_footer = models.CharField(max_length=100, blank=True)

    join_us_title = models.CharField(max_length=100, blank=True)
    join_us_subtitle = models.CharField(max_length=100, blank=True)
    join_us_text = models.CharField(max_length=100, blank=True)
    join_us_image_1 = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    join_us_image_2 = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    join_us_infos = StreamField([("info", InfoItemBlock())], null=True, blank=True, verbose_name="Join Us Info")

    cta_title = models.CharField(max_length=100, blank=True, verbose_name="CTA Title")
    cta_subtitle = models.CharField(max_length=100, blank=True, verbose_name="CTA Subtitle")
    cta_button1 = models.CharField(max_length=100, blank=True, verbose_name="Request Gig Button")
    cta_button2 = models.CharField(max_length=100, blank=True, verbose_name="Contact Us Button")

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("menu_festival"),
                FieldPanel("menu_who_we_are"),
                FieldPanel("menu_upcoming_gigs"),
                FieldPanel("menu_merch"),
                FieldPanel("menu_join_us"),
                FieldPanel("menu_request_gig"),
                FieldPanel("menu_contact"),
            ],
            "Menu Navigation",
        ),
        MultiFieldPanel(
            [
                FieldPanel("about_text"),
                FieldPanel("whoweare_title"),
                FieldPanel("whoweare_text"),
                FieldPanel("whoweare_gallery"),
            ],
            "About SNO",
        ),
        MultiFieldPanel(
            [
                FieldPanel("gigs_title"),
                FieldPanel("gigs_subtitle"),
            ],
            "Gigs",
        ),
        MultiFieldPanel(
            [
                FieldPanel("merch_title"),
                FieldPanel("merch_subtitle"),
                FieldPanel("merch_text"),
                FieldPanel("merch_items"),
            ],
            "Merch",
        ),
        MultiFieldPanel(
            [
                FieldPanel("donate_title"),
                FieldPanel("donate_online"),
                FieldPanel("donate_offline"),
                FieldPanel("donate_footer"),
            ],
            "Donate",
        ),
        MultiFieldPanel(
            [
                FieldPanel("join_us_title"),
                FieldPanel("join_us_subtitle"),
                FieldPanel("join_us_text"),
                FieldPanel("join_us_image_1"),
                FieldPanel("join_us_image_2"),
                FieldPanel("join_us_infos"),
            ],
            "Join Us",
        ),
        MultiFieldPanel(
            [
                FieldPanel("cta_title"),
                FieldPanel("cta_subtitle"),
                FieldPanel("cta_button1"),
                FieldPanel("cta_button2"),
            ],
            "Call To Action + Footer",
        ),
    ]

    def get_context(self, request):
        from home.forms import DonationForm

        context = super(HomePage2, self).get_context(request)
        donation_page = DonationPage.objects.first()
        if donation_page is not None:
            url = donation_page.get_url()
            context["donation_form"] = DonationForm()
            context["donation_page_url"] = url

        context["blogs"] = self.blogs()
        context["gigs"] = self.gigs()
        context["homepage"] = self
        return context

    def gigs(self):
        from gigs.models import GigPage

        gigs = GigPage.objects.filter(live=True)
        gigs = gigs.filter(date_from__gte=date.today())
        gigs = gigs.all().order_by("date_from")
        return gigs

    def get_blog_index(self):
        return BlogIndexPage.objects.first()

    def blogs(self):
        return self.get_blog_index().blogindexpage.blogs


class FestivalPage(Page):
    menu_festival = models.CharField(max_length=100, blank=True)
    menu_who_we_are = models.CharField(max_length=100, blank=True)
    menu_upcoming_gigs = models.CharField(max_length=100, blank=True)
    menu_merch = models.CharField(max_length=100, blank=True)
    menu_join_us = models.CharField(max_length=100, blank=True)
    menu_request_gig = models.CharField(max_length=100, blank=True)
    menu_contact = models.CharField(max_length=100, blank=True)
    festival_intro_title = models.CharField(max_length=100, blank=True)
    festival_intro_title2 = models.CharField(max_length=100, blank=True)
    festival_intro_text = RichTextField(blank=True, features=["bold", "italic", "link"])
    festival_intro_text2 = RichTextField(blank=True, features=["bold", "italic", "link"])
    festival_intro_footer = RichTextField(blank=True, features=["bold", "italic", "link"])
    festival_program_title = models.CharField(max_length=100, blank=True)
    festival_program_timeline = StreamField(
        [
            ("heading", TimelineHeaderBlock(label="Timeline Heading")),
            ("item", TimelineItemBlock(label="Timeline Item")),
        ],
        null=True,
        blank=True,
    )
    festival_program_content = StreamField(
        [
            ("heading", blocks.CharBlock(classname="full title")),
            ("paragraph", blocks.RichTextBlock()),
        ],
        null=True,
        blank=True,
    )

    about_text = RichTextField(blank=True, features=["bold", "italic", "link"], verbose_name="About SNO")
    whoweare_title = models.CharField(max_length=100, blank=True, verbose_name="Who We Are title")
    whoweare_text = RichTextField(blank=True, features=["bold", "italic", "link"], verbose_name="Who We Are text")
    whoweare_gallery = StreamField(
        [
            ("image", ImageChooserBlock(label="Gallery Image")),
        ],
        null=True,
        blank=True,
        verbose_name="Who We Are Gallery",
    )

    gigs_title = models.CharField(max_length=100, blank=True)
    gigs_subtitle = models.CharField(max_length=100, blank=True)

    merch_title = models.CharField(max_length=100, blank=True)
    merch_subtitle = models.CharField(max_length=100, blank=True)
    merch_text = RichTextField(blank=True, features=["bold", "italic", "link"], verbose_name="Merch Detail")
    merch_items = StreamField(
        [
            ("merch", MerchItemBlock(label="Merch Item")),
        ],
        null=True,
        blank=True,
        verbose_name="Merchandise",
    )

    donate_title = models.CharField(max_length=100, blank=True)
    donate_online = models.CharField(max_length=100, blank=True)
    donate_offline = models.CharField(max_length=100, blank=True)
    donate_footer = models.CharField(max_length=100, blank=True)

    join_us_title = models.CharField(max_length=100, blank=True)
    join_us_subtitle = models.CharField(max_length=100, blank=True)
    join_us_text = models.CharField(max_length=100, blank=True)
    join_us_image_1 = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    join_us_image_2 = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    join_us_infos = StreamField([("info", InfoItemBlock())], null=True, blank=True, verbose_name="Join Us Info")

    cta_title = models.CharField(max_length=100, blank=True, verbose_name="CTA Title")
    cta_subtitle = models.CharField(max_length=100, blank=True, verbose_name="CTA Subtitle")
    cta_button1 = models.CharField(max_length=100, blank=True, verbose_name="Request Gig Button")
    cta_button2 = models.CharField(max_length=100, blank=True, verbose_name="Contact Us Button")

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("menu_festival"),
                FieldPanel("menu_who_we_are"),
                FieldPanel("menu_upcoming_gigs"),
                FieldPanel("menu_merch"),
                FieldPanel("menu_join_us"),
                FieldPanel("menu_request_gig"),
                FieldPanel("menu_contact"),
            ],
            "Menu Navigation",
        ),
        MultiFieldPanel(
            [
                FieldPanel("festival_intro_title"),
                FieldPanel("festival_intro_text"),
                InlinePanel("festival_bands", label="Bands"),
                FieldPanel("festival_intro_title2"),
                FieldPanel("festival_intro_text2"),
                FieldPanel("festival_intro_footer"),
            ],
            "Festival Intro",
        ),
        MultiFieldPanel(
            [
                FieldPanel("festival_program_title"),
                FieldPanel("festival_program_content"),
                FieldPanel("festival_program_timeline"),
            ],
            "Festival Program",
        ),
        MultiFieldPanel(
            [
                FieldPanel("about_text"),
                FieldPanel("whoweare_title"),
                FieldPanel("whoweare_text"),
                FieldPanel("whoweare_gallery"),
            ],
            "About SNO",
        ),
        MultiFieldPanel(
            [
                FieldPanel("gigs_title"),
                FieldPanel("gigs_subtitle"),
            ],
            "Gigs",
        ),
        MultiFieldPanel(
            [
                FieldPanel("merch_title"),
                FieldPanel("merch_subtitle"),
                FieldPanel("merch_text"),
                FieldPanel("merch_items"),
            ],
            "Merch",
        ),
        MultiFieldPanel(
            [
                FieldPanel("donate_title"),
                FieldPanel("donate_online"),
                FieldPanel("donate_offline"),
                FieldPanel("donate_footer"),
            ],
            "Donate",
        ),
        MultiFieldPanel(
            [
                FieldPanel("join_us_title"),
                FieldPanel("join_us_subtitle"),
                FieldPanel("join_us_text"),
                FieldPanel("join_us_image_1"),
                FieldPanel("join_us_image_2"),
                FieldPanel("join_us_infos"),
            ],
            "Join Us",
        ),
        MultiFieldPanel(
            [
                FieldPanel("cta_title"),
                FieldPanel("cta_subtitle"),
                FieldPanel("cta_button1"),
                FieldPanel("cta_button2"),
            ],
            "Call To Action + Footer",
        ),
    ]

    def get_context(self, request):
        from home.forms import DonationForm

        context = super(FestivalPage, self).get_context(request)
        donation_page = DonationPage.objects.first()
        if donation_page is not None:
            url = donation_page.get_url()
            context["donation_form"] = DonationForm()
            context["donation_page_url"] = url
        return context


@register_snippet
class GigType(models.Model):
    """
    A Django model to define the gig type, used in the gig request form.
    It uses the `@register_snippet` decorator to allow it to be accessible
    via the Snippets UI.
    """

    name = models.CharField(max_length=255)

    panels = [
        FieldPanel("name"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Gig Types"


class GigRequest(models.Model):
    contact_name = models.CharField(max_length=100, blank=True)
    contact_email = models.CharField(max_length=100, blank=True)
    event_date = models.DateField()
    event_time = models.TimeField(null=True, blank=True)
    deadline_date = models.DateField()
    event_type = models.CharField(max_length=100, blank=True)
    event_occasion = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=255, blank=True)
    donation_amount = models.IntegerField(blank=True)
    details = models.CharField(max_length=255, blank=True)


class GigRequestPage(Page):
    intro_text = RichTextField(blank=True, features=["bold", "italic", "link"])
    label_contact_name = models.CharField(max_length=100, blank=True)
    label_contact_email = models.CharField(max_length=100, blank=True)
    label_contact_org = models.CharField(max_length=100, blank=True, verbose_name="Label Contact Organization")
    label_event_date = models.CharField(max_length=100, blank=True)
    label_event_time = models.CharField(max_length=100, blank=True)
    label_deadline_date = models.CharField(max_length=100, blank=True)
    label_deadline_detail = models.CharField(max_length=255, blank=True)
    label_event_type = models.CharField(max_length=100, blank=True)
    label_event_occasion = models.CharField(max_length=100, blank=True)
    label_event_occasion_example = models.CharField(max_length=255, blank=True)
    label_location = models.CharField(max_length=255, blank=True)
    label_donation_amount = models.CharField(max_length=100, blank=True)
    label_donation_detail = models.CharField(max_length=255, blank=True)
    details_title = models.CharField(max_length=100, blank=True)
    details = RichTextField(blank=True, features=["bold", "italic", "link", "ol", "ul"])

    thank_you = models.CharField(max_length=100, blank=True)
    thank_you_text = RichTextField(blank=True, features=["bold", "italic", "link", "ol", "ul"])

    content_panels = Page.content_panels + [
        FieldPanel("intro_text"),
        FieldPanel("label_contact_name"),
        FieldPanel("label_contact_email"),
        FieldPanel("label_contact_org"),
        FieldPanel("label_event_date"),
        FieldPanel("label_event_time"),
        FieldPanel("label_deadline_date"),
        FieldPanel("label_deadline_detail"),
        FieldPanel("label_event_type"),
        FieldPanel("label_event_occasion"),
        FieldPanel("label_event_occasion_example"),
        FieldPanel("label_location"),
        FieldPanel("label_donation_amount"),
        FieldPanel("label_donation_detail"),
        FieldPanel("details_title"),
        FieldPanel("details"),
        FieldPanel("thank_you"),
        FieldPanel("thank_you_text"),
    ]

    def serve(self, request):
        from home.forms import GigRequestForm

        if request.method == "POST":
            form = GigRequestForm(request.POST)
            if form.is_valid():
                success = send_form_mail(form)
                if success:
                    return render(
                        request,
                        "home/gig_request_thank_you.html",
                        {"page": self, "form": form},
                    )
                else:
                    return render(
                        request,
                        "home/gig_request_error.html",
                        {"page": self, "form": form},
                    )
        else:
            form = GigRequestForm()

        return render(
            request,
            "home/gig_request_form.html",
            {
                "page": self,
                "form": form,
            },
        )


def send_form_mail(form):
    message = """
    Liebe Band,

    Someone requested a gig from the website:

    Name:  {contact_name}
    Organization:  {contact_org}
    Email: {contact_email}

    Date: {event_date}
    Time: {event_time}
    Deadline to decide: {deadline_date}

    Event Type: {event_type}
    Occasion: {event_occasion}

    Location: {location}

    Donation: {donation_amount}

    Details:
    {details}

    """.format(
        **form.cleaned_data
    ).strip()

    sender = "StreetNoise Orchestra <website@notifications.streetnoise.at>"
    recipients = settings.CONTACT_FORM_RECIPIENTS

    subject = "Gig Request from {contact_name} @ {contact_org}".format(**form.cleaned_data)
    send_mail(subject, message, sender, recipients)
    return True


class GenericPage(Page):
    content = StreamField(
        [
            ("heading", blocks.CharBlock()),
            (
                "paragraph",
                blocks.RichTextBlock(
                    features=[
                        "h1",
                        "h2",
                        "h3",
                        "h4",
                        "h5",
                        "bold",
                        "italic",
                        "strikethrough",
                        "ol",
                        "ul",
                        "hr",
                        "link",
                        "document-link",
                        "image",
                        "embed",
                        "blockquote",
                    ]
                ),
            ),
            ("image", ImageChooserBlock(icon="image")),
            ("rawhtml", blocks.RawHTMLBlock()),
            ("quote", blocks.BlockQuoteBlock()),
            (
                "embed",
                EmbedBlock(
                    icon="media",
                    label=_("Embed media"),
                    help_text=_("Paste a link to a video, audio file, instagram, etc."),
                ),
            ),
            ("imagetile", ImageTileBlock()),
            ("imagetile2", ImageTileBlock2()),
            ("footercta", FooterCTABlock()),
            ("newsletter_signup", NewsletterSignupBlock()),
            ("image_grid", ImageGridBlock()),
            ("paragraph_image", ParagraphImageBlock()),
        ],
        null=True,
        blank=True,
    )

    cta_title = models.CharField(max_length=100, blank=True, verbose_name="CTA Title")
    cta_subtitle = models.CharField(max_length=100, blank=True, verbose_name="CTA Subtitle")
    cta_button1 = models.CharField(max_length=100, blank=True, verbose_name="CTA Button 1 Text")
    cta_button1_url = models.CharField(max_length=100, blank=True, verbose_name="CTA Button 1 Link")
    cta_button2 = models.CharField(max_length=100, blank=True, verbose_name="CTA Button 2 Text")
    cta_button2_url = models.CharField(max_length=100, blank=True, verbose_name="CTA Button 2 Link")

    content_panels = Page.content_panels + [
        FieldPanel("content"),
        MultiFieldPanel(
            [
                FieldPanel("cta_title"),
                FieldPanel("cta_subtitle"),
                FieldPanel("cta_button1"),
                FieldPanel("cta_button1_url"),
                FieldPanel("cta_button2"),
                FieldPanel("cta_button2_url"),
            ],
            "Call To Action + Footer",
        ),
    ]

    def get_context(self, request):
        context = super(GenericPage, self).get_context(request)
        homepage = HomePage2.objects.first()
        context["homepage"] = homepage
        return context


class DonationPage(Page):
    donation_intro = StreamField(
        [
            ("heading", blocks.CharBlock()),
            ("paragraph", blocks.RichTextBlock()),
        ],
        null=True,
        blank=True,
    )

    label_donation_amount = models.CharField(max_length=100, blank=True)
    label_donation = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Donation line item",
        help_text='The word "donation" used on the official donation receipt',
    )
    label_donation_detail = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Donation line item description",
        help_text="A small description of the donation used on the official donation receipt",
    )

    thank_you = models.CharField(
        max_length=100,
        blank=True,
        help_text="The title displayed after the user successful donates.",
    )
    thank_you_text = RichTextField(
        blank=True,
        features=["bold", "italic", "link", "ol", "ul"],
        help_text="Text displayed after the user successful donates.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("donation_intro"),
        FieldPanel("label_donation_amount"),
        FieldPanel("label_donation"),
        FieldPanel("label_donation_detail"),
        FieldPanel("thank_you"),
        FieldPanel("thank_you_text"),
    ]

    def serve(self, request):
        import stripe
        from django.templatetags.static import static
        from home.forms import DonationForm

        site = Site.find_for_request(request)

        if request.method == "POST":
            form = DonationForm(request.POST)
            if form.is_valid():
                img_url = "{}{}".format(site.root_url, static("/img/unterstuetzen.jpg"))
                stripe.api_key = settings.STRIPE_SK
                session = stripe.checkout.Session.create(
                    payment_method_types=["card"],
                    line_items=[
                        {
                            "name": self.label_donation,
                            "description": self.label_donation_detail,
                            "images": [img_url],
                            "amount": 100 * form.cleaned_data["donation_amount"],
                            "currency": "eur",
                            "quantity": 1,
                        }
                    ],
                    success_url="{}?checkout=success".format(self.get_full_url()),
                    cancel_url=site.root_url,
                )
                self.checkout_session_id = session.id
                self.stripe_pk = settings.STRIPE_PK
                return render(request, "home/donation_checkout.html", {"page": self, "form": form})
        elif request.GET.get("checkout", False) == "success":
            return render(request, "home/donation_success.html", {"page": self})
        elif request.GET.get("amount"):
            form = DonationForm(initial={"donation_amount": request.GET.get("amount", 0)})
        else:
            form = DonationForm()

        return render(
            request,
            "home/donation_page.html",
            {
                "page": self,
                "form": form,
            },
        )
