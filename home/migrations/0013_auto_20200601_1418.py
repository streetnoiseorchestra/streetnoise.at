# Generated by Django 2.2.3 on 2020-06-01 14:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("wagtailimages", "0022_uploadedimage"),
        ("wagtailcore", "0045_assign_unlock_grouppagepermission"),
        ("contenttypes", "0002_remove_content_type_name"),
        ("home", "0012_auto_20190726_1722"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="HomePage",
            new_name="FestivalPage",
        ),
    ]
