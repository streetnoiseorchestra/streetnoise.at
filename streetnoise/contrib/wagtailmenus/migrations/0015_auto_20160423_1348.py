# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailmenus", "0014_auto_20160423_1339"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flatmenuitem",
            name="allow_subnav",
            field=models.BooleanField(
                default=False,
                help_text="NOTE: The sub-menu might not be displayed, even if checked. It depends on how the menu is used in this project's templates.",
                verbose_name="allow sub-menu for this item",
            ),
        ),
        migrations.AlterField(
            model_name="mainmenuitem",
            name="allow_subnav",
            field=models.BooleanField(
                default=True,
                help_text="NOTE: The sub-menu might not be displayed, even if checked. It depends on how the menu is used in this project's templates.",
                verbose_name="allow sub-menu for this item",
            ),
        ),
    ]
