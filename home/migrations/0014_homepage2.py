# Generated by Django 3.0.6 on 2020-06-02 07:03

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailimages", "0022_uploadedimage"),
        ("wagtailcore", "0045_assign_unlock_grouppagepermission"),
        ("home", "0013_auto_20200601_1418"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomePage2",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                ("menu_festival", models.CharField(blank=True, max_length=100)),
                ("menu_festival_de", models.CharField(blank=True, max_length=100, null=True)),
                ("menu_festival_en", models.CharField(blank=True, max_length=100, null=True)),
                ("menu_who_we_are", models.CharField(blank=True, max_length=100)),
                ("menu_who_we_are_de", models.CharField(blank=True, max_length=100, null=True)),
                ("menu_who_we_are_en", models.CharField(blank=True, max_length=100, null=True)),
                ("menu_upcoming_gigs", models.CharField(blank=True, max_length=100)),
                ("menu_upcoming_gigs_de", models.CharField(blank=True, max_length=100, null=True)),
                ("menu_upcoming_gigs_en", models.CharField(blank=True, max_length=100, null=True)),
                ("menu_merch", models.CharField(blank=True, max_length=100)),
                ("menu_merch_de", models.CharField(blank=True, max_length=100, null=True)),
                ("menu_merch_en", models.CharField(blank=True, max_length=100, null=True)),
                ("menu_join_us", models.CharField(blank=True, max_length=100)),
                ("menu_join_us_de", models.CharField(blank=True, max_length=100, null=True)),
                ("menu_join_us_en", models.CharField(blank=True, max_length=100, null=True)),
                ("menu_request_gig", models.CharField(blank=True, max_length=100)),
                ("menu_request_gig_de", models.CharField(blank=True, max_length=100, null=True)),
                ("menu_request_gig_en", models.CharField(blank=True, max_length=100, null=True)),
                ("menu_contact", models.CharField(blank=True, max_length=100)),
                ("menu_contact_de", models.CharField(blank=True, max_length=100, null=True)),
                ("menu_contact_en", models.CharField(blank=True, max_length=100, null=True)),
                ("about_text", wagtail.fields.RichTextField(blank=True, verbose_name="About SNO")),
                ("about_text_de", wagtail.fields.RichTextField(blank=True, null=True, verbose_name="About SNO")),
                ("about_text_en", wagtail.fields.RichTextField(blank=True, null=True, verbose_name="About SNO")),
                ("whoweare_title", models.CharField(blank=True, max_length=100, verbose_name="Who We Are title")),
                (
                    "whoweare_title_de",
                    models.CharField(blank=True, max_length=100, null=True, verbose_name="Who We Are title"),
                ),
                (
                    "whoweare_title_en",
                    models.CharField(blank=True, max_length=100, null=True, verbose_name="Who We Are title"),
                ),
                ("whoweare_text", wagtail.fields.RichTextField(blank=True, verbose_name="Who We Are text")),
                (
                    "whoweare_text_de",
                    wagtail.fields.RichTextField(blank=True, null=True, verbose_name="Who We Are text"),
                ),
                (
                    "whoweare_text_en",
                    wagtail.fields.RichTextField(blank=True, null=True, verbose_name="Who We Are text"),
                ),
                (
                    "whoweare_gallery",
                    wagtail.fields.StreamField(
                        [("image", wagtail.images.blocks.ImageChooserBlock(label="Gallery Image"))],
                        blank=True,
                        null=True,
                        verbose_name="Who We Are Gallery",
                    ),
                ),
                ("gigs_title", models.CharField(blank=True, max_length=100)),
                ("gigs_title_de", models.CharField(blank=True, max_length=100, null=True)),
                ("gigs_title_en", models.CharField(blank=True, max_length=100, null=True)),
                ("gigs_subtitle", models.CharField(blank=True, max_length=100)),
                ("gigs_subtitle_de", models.CharField(blank=True, max_length=100, null=True)),
                ("gigs_subtitle_en", models.CharField(blank=True, max_length=100, null=True)),
                ("merch_title", models.CharField(blank=True, max_length=100)),
                ("merch_title_de", models.CharField(blank=True, max_length=100, null=True)),
                ("merch_title_en", models.CharField(blank=True, max_length=100, null=True)),
                ("merch_subtitle", models.CharField(blank=True, max_length=100)),
                ("merch_subtitle_de", models.CharField(blank=True, max_length=100, null=True)),
                ("merch_subtitle_en", models.CharField(blank=True, max_length=100, null=True)),
                ("merch_text", wagtail.fields.RichTextField(blank=True, verbose_name="Merch Detail")),
                ("merch_text_de", wagtail.fields.RichTextField(blank=True, null=True, verbose_name="Merch Detail")),
                ("merch_text_en", wagtail.fields.RichTextField(blank=True, null=True, verbose_name="Merch Detail")),
                (
                    "merch_items",
                    wagtail.fields.StreamField(
                        [
                            (
                                "merch",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("image", wagtail.images.blocks.ImageChooserBlock()),
                                        ("title", wagtail.blocks.CharBlock()),
                                        ("price", wagtail.blocks.CharBlock()),
                                        ("detail", wagtail.blocks.CharBlock()),
                                    ],
                                    label="Merch Item",
                                ),
                            )
                        ],
                        blank=True,
                        null=True,
                        verbose_name="Merchandise",
                    ),
                ),
                (
                    "merch_items_de",
                    wagtail.fields.StreamField(
                        [
                            (
                                "merch",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("image", wagtail.images.blocks.ImageChooserBlock()),
                                        ("title", wagtail.blocks.CharBlock()),
                                        ("price", wagtail.blocks.CharBlock()),
                                        ("detail", wagtail.blocks.CharBlock()),
                                    ],
                                    label="Merch Item",
                                ),
                            )
                        ],
                        blank=True,
                        null=True,
                        verbose_name="Merchandise",
                    ),
                ),
                (
                    "merch_items_en",
                    wagtail.fields.StreamField(
                        [
                            (
                                "merch",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("image", wagtail.images.blocks.ImageChooserBlock()),
                                        ("title", wagtail.blocks.CharBlock()),
                                        ("price", wagtail.blocks.CharBlock()),
                                        ("detail", wagtail.blocks.CharBlock()),
                                    ],
                                    label="Merch Item",
                                ),
                            )
                        ],
                        blank=True,
                        null=True,
                        verbose_name="Merchandise",
                    ),
                ),
                ("donate_title", models.CharField(blank=True, max_length=100)),
                ("donate_title_de", models.CharField(blank=True, max_length=100, null=True)),
                ("donate_title_en", models.CharField(blank=True, max_length=100, null=True)),
                ("donate_online", models.CharField(blank=True, max_length=100)),
                ("donate_online_de", models.CharField(blank=True, max_length=100, null=True)),
                ("donate_online_en", models.CharField(blank=True, max_length=100, null=True)),
                ("donate_offline", models.CharField(blank=True, max_length=100)),
                ("donate_offline_de", models.CharField(blank=True, max_length=100, null=True)),
                ("donate_offline_en", models.CharField(blank=True, max_length=100, null=True)),
                ("donate_footer", models.CharField(blank=True, max_length=100)),
                ("donate_footer_de", models.CharField(blank=True, max_length=100, null=True)),
                ("donate_footer_en", models.CharField(blank=True, max_length=100, null=True)),
                ("join_us_title", models.CharField(blank=True, max_length=100)),
                ("join_us_title_de", models.CharField(blank=True, max_length=100, null=True)),
                ("join_us_title_en", models.CharField(blank=True, max_length=100, null=True)),
                ("join_us_subtitle", models.CharField(blank=True, max_length=100)),
                ("join_us_subtitle_de", models.CharField(blank=True, max_length=100, null=True)),
                ("join_us_subtitle_en", models.CharField(blank=True, max_length=100, null=True)),
                ("join_us_text", models.CharField(blank=True, max_length=100)),
                ("join_us_text_de", models.CharField(blank=True, max_length=100, null=True)),
                ("join_us_text_en", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "join_us_infos",
                    wagtail.fields.StreamField(
                        [
                            (
                                "info",
                                wagtail.blocks.StructBlock(
                                    [("title", wagtail.blocks.CharBlock()), ("detail", wagtail.blocks.RichTextBlock())]
                                ),
                            )
                        ],
                        blank=True,
                        null=True,
                        verbose_name="Join Us Info",
                    ),
                ),
                (
                    "join_us_infos_de",
                    wagtail.fields.StreamField(
                        [
                            (
                                "info",
                                wagtail.blocks.StructBlock(
                                    [("title", wagtail.blocks.CharBlock()), ("detail", wagtail.blocks.RichTextBlock())]
                                ),
                            )
                        ],
                        blank=True,
                        null=True,
                        verbose_name="Join Us Info",
                    ),
                ),
                (
                    "join_us_infos_en",
                    wagtail.fields.StreamField(
                        [
                            (
                                "info",
                                wagtail.blocks.StructBlock(
                                    [("title", wagtail.blocks.CharBlock()), ("detail", wagtail.blocks.RichTextBlock())]
                                ),
                            )
                        ],
                        blank=True,
                        null=True,
                        verbose_name="Join Us Info",
                    ),
                ),
                ("cta_title", models.CharField(blank=True, max_length=100, verbose_name="CTA Title")),
                ("cta_title_de", models.CharField(blank=True, max_length=100, null=True, verbose_name="CTA Title")),
                ("cta_title_en", models.CharField(blank=True, max_length=100, null=True, verbose_name="CTA Title")),
                ("cta_subtitle", models.CharField(blank=True, max_length=100, verbose_name="CTA Subtitle")),
                (
                    "cta_subtitle_de",
                    models.CharField(blank=True, max_length=100, null=True, verbose_name="CTA Subtitle"),
                ),
                (
                    "cta_subtitle_en",
                    models.CharField(blank=True, max_length=100, null=True, verbose_name="CTA Subtitle"),
                ),
                ("cta_button1", models.CharField(blank=True, max_length=100, verbose_name="Request Gig Button")),
                (
                    "cta_button1_de",
                    models.CharField(blank=True, max_length=100, null=True, verbose_name="Request Gig Button"),
                ),
                (
                    "cta_button1_en",
                    models.CharField(blank=True, max_length=100, null=True, verbose_name="Request Gig Button"),
                ),
                ("cta_button2", models.CharField(blank=True, max_length=100, verbose_name="Contact Us Button")),
                (
                    "cta_button2_de",
                    models.CharField(blank=True, max_length=100, null=True, verbose_name="Contact Us Button"),
                ),
                (
                    "cta_button2_en",
                    models.CharField(blank=True, max_length=100, null=True, verbose_name="Contact Us Button"),
                ),
                (
                    "feed_image",
                    models.ForeignKey(
                        blank=True,
                        help_text="The image shown on Facebook and other social media",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.Image",
                    ),
                ),
                (
                    "join_us_image_1",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.Image",
                    ),
                ),
                (
                    "join_us_image_2",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.Image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
