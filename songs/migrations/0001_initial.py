# Generated by Django 4.1.13 on 2023-11-20 13:49

import uuid

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0083_workflowcontenttype"),
    ]

    operations = [
        migrations.CreateModel(
            name="SongIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="SongPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("snorga_id", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("arrangement_credits", models.CharField(blank=True, max_length=255, null=True)),
                ("composition_credits", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "description",
                    wagtail.fields.RichTextField(
                        blank=True, help_text="A sentence or two describing the song.", verbose_name="Description"
                    ),
                ),
                (
                    "description_de",
                    wagtail.fields.RichTextField(
                        blank=True,
                        help_text="A sentence or two describing the song.",
                        null=True,
                        verbose_name="Description",
                    ),
                ),
                (
                    "description_en",
                    wagtail.fields.RichTextField(
                        blank=True,
                        help_text="A sentence or two describing the song.",
                        null=True,
                        verbose_name="Description",
                    ),
                ),
                (
                    "arrangement_notes",
                    wagtail.fields.RichTextField(
                        blank=True, help_text="Our notes for the arrangement", verbose_name="Details"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]