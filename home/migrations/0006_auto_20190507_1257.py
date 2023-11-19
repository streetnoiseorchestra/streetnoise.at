# Generated by Django 2.2.1 on 2019-05-07 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0005_auto_20190507_1256"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="feed_image",
            field=models.ForeignKey(
                blank=True,
                help_text="The image shown on Facebook and other social media",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.Image",
            ),
        ),
    ]
