# Generated by Django 2.2.1 on 2019-05-06 09:32

import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
        ("wagtailimages", "0001_squashed_0021"),
    ]

    operations = [
        migrations.CreateModel(
            name="BandFriend",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("website", models.URLField()),
                ("facebook", models.URLField()),
                (
                    "square_logo",
                    models.ForeignKey(
                        blank=True,
                        help_text="Square logo image; between 128px and 1000px",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.Image",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Band friends",
            },
        ),
        migrations.CreateModel(
            name="GigRequest",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("contact_name", models.CharField(blank=True, max_length=100)),
                ("contact_email", models.CharField(blank=True, max_length=100)),
                ("event_date", models.DateField()),
                ("event_time", models.TimeField(blank=True, null=True)),
                ("deadline_date", models.DateField()),
                ("event_type", models.CharField(blank=True, max_length=100)),
                ("event_occasion", models.CharField(blank=True, max_length=100)),
                ("location", models.CharField(blank=True, max_length=255)),
                ("donation_amount", models.IntegerField(blank=True)),
                ("details", models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="GigRequestPage",
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
                ("intro_text", wagtail.fields.RichTextField(blank=True)),
                ("label_contact_name", models.CharField(blank=True, max_length=100)),
                ("label_contact_email", models.CharField(blank=True, max_length=100)),
                (
                    "label_contact_org",
                    models.CharField(blank=True, max_length=100, verbose_name="Label Contact Organization"),
                ),
                ("label_event_date", models.CharField(blank=True, max_length=100)),
                ("label_event_time", models.CharField(blank=True, max_length=100)),
                ("label_deadline_date", models.CharField(blank=True, max_length=100)),
                ("label_deadline_detail", models.CharField(blank=True, max_length=255)),
                ("label_event_type", models.CharField(blank=True, max_length=100)),
                ("label_event_occasion", models.CharField(blank=True, max_length=100)),
                ("label_event_occasion_example", models.CharField(blank=True, max_length=255)),
                ("label_location", models.CharField(blank=True, max_length=255)),
                ("label_donation_amount", models.CharField(blank=True, max_length=100)),
                ("label_donation_detail", models.CharField(blank=True, max_length=255)),
                ("details_title", models.CharField(blank=True, max_length=100)),
                ("details", wagtail.fields.RichTextField(blank=True)),
                ("thank_you", models.CharField(blank=True, max_length=100)),
                ("thank_you_text", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="GigType",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("name_de", models.CharField(max_length=255, null=True)),
                ("name_en", models.CharField(max_length=255, null=True)),
            ],
            options={
                "verbose_name_plural": "Gig Types",
            },
        ),
        migrations.CreateModel(
            name="HomePage",
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
                ("subtitle", models.CharField(blank=True, max_length=100)),
                ("festival_intro_title", models.CharField(blank=True, max_length=100)),
                ("festival_intro_title_de", models.CharField(blank=True, max_length=100, null=True)),
                ("festival_intro_title_en", models.CharField(blank=True, max_length=100, null=True)),
                ("festival_intro_title2", models.CharField(blank=True, max_length=100)),
                ("festival_intro_title2_de", models.CharField(blank=True, max_length=100, null=True)),
                ("festival_intro_title2_en", models.CharField(blank=True, max_length=100, null=True)),
                ("festival_intro_text", wagtail.fields.RichTextField(blank=True)),
                ("festival_intro_text_de", wagtail.fields.RichTextField(blank=True, null=True)),
                ("festival_intro_text_en", wagtail.fields.RichTextField(blank=True, null=True)),
                ("festival_intro_text2", wagtail.fields.RichTextField(blank=True)),
                ("festival_intro_text2_de", wagtail.fields.RichTextField(blank=True, null=True)),
                ("festival_intro_text2_en", wagtail.fields.RichTextField(blank=True, null=True)),
                ("festival_intro_footer", wagtail.fields.RichTextField(blank=True)),
                ("festival_intro_footer_de", wagtail.fields.RichTextField(blank=True, null=True)),
                ("festival_intro_footer_en", wagtail.fields.RichTextField(blank=True, null=True)),
                ("festival_program_title", models.CharField(blank=True, max_length=100)),
                ("festival_program_title_de", models.CharField(blank=True, max_length=100, null=True)),
                ("festival_program_title_en", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "festival_program_timeline",
                    wagtail.fields.StreamField(
                        [
                            (
                                "heading",
                                wagtail.blocks.StructBlock(
                                    [("title", wagtail.blocks.CharBlock())], label="Timeline Heading"
                                ),
                            ),
                            (
                                "item",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("icon", wagtail.blocks.CharBlock()),
                                        ("title", wagtail.blocks.CharBlock(label="Time")),
                                        ("detail", wagtail.blocks.CharBlock(label="Name")),
                                        (
                                            "small_detail",
                                            wagtail.blocks.CharBlock(label="Extra Detail", required=False),
                                        ),
                                    ],
                                    label="Timeline Item",
                                ),
                            ),
                        ],
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "festival_program_timeline_de",
                    wagtail.fields.StreamField(
                        [
                            (
                                "heading",
                                wagtail.blocks.StructBlock(
                                    [("title", wagtail.blocks.CharBlock())], label="Timeline Heading"
                                ),
                            ),
                            (
                                "item",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("icon", wagtail.blocks.CharBlock()),
                                        ("title", wagtail.blocks.CharBlock(label="Time")),
                                        ("detail", wagtail.blocks.CharBlock(label="Name")),
                                        (
                                            "small_detail",
                                            wagtail.blocks.CharBlock(label="Extra Detail", required=False),
                                        ),
                                    ],
                                    label="Timeline Item",
                                ),
                            ),
                        ],
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "festival_program_timeline_en",
                    wagtail.fields.StreamField(
                        [
                            (
                                "heading",
                                wagtail.blocks.StructBlock(
                                    [("title", wagtail.blocks.CharBlock())], label="Timeline Heading"
                                ),
                            ),
                            (
                                "item",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("icon", wagtail.blocks.CharBlock()),
                                        ("title", wagtail.blocks.CharBlock(label="Time")),
                                        ("detail", wagtail.blocks.CharBlock(label="Name")),
                                        (
                                            "small_detail",
                                            wagtail.blocks.CharBlock(label="Extra Detail", required=False),
                                        ),
                                    ],
                                    label="Timeline Item",
                                ),
                            ),
                        ],
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "festival_program_content",
                    wagtail.fields.StreamField(
                        [
                            ("heading", wagtail.blocks.CharBlock(classname="full title")),
                            ("paragraph", wagtail.blocks.RichTextBlock()),
                        ],
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "festival_program_content_de",
                    wagtail.fields.StreamField(
                        [
                            ("heading", wagtail.blocks.CharBlock(classname="full title")),
                            ("paragraph", wagtail.blocks.RichTextBlock()),
                        ],
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "festival_program_content_en",
                    wagtail.fields.StreamField(
                        [
                            ("heading", wagtail.blocks.CharBlock(classname="full title")),
                            ("paragraph", wagtail.blocks.RichTextBlock()),
                        ],
                        blank=True,
                        null=True,
                    ),
                ),
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
        migrations.CreateModel(
            name="HomePageBandFriend",
            fields=[
                (
                    "bandfriend_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="home.BandFriend",
                    ),
                ),
                ("sort_order", models.IntegerField(blank=True, editable=False, null=True)),
                (
                    "band_friend",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="band_friends", to="home.BandFriend"
                    ),
                ),
                (
                    "home_page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="festival_bands", to="home.HomePage"
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
            bases=("home.bandfriend", models.Model),
        ),
    ]
