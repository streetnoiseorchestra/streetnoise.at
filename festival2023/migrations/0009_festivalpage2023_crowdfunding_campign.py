# Generated by Django 4.0.8 on 2023-05-03 06:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("festival2023", "0008_alter_festivalpage2023_body_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="festivalpage2023",
            name="crowdfunding_campign",
            field=models.CharField(choices=[("test", "test")], default="festival2023/homepage.html", max_length=255),
        ),
    ]
