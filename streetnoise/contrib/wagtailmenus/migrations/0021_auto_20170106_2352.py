# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-06 23:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailmenus", "0020_auto_20161210_0004"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="flatmenuitem",
            options={"ordering": ("sort_order",)},
        ),
        migrations.AlterModelOptions(
            name="mainmenuitem",
            options={"ordering": ("sort_order",)},
        ),
    ]
