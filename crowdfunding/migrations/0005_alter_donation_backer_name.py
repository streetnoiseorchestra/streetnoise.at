# Generated by Django 4.1.9 on 2023-06-08 07:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crowdfunding", "0004_campaign_stretch_goal1_campaign_stretch_goal2"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donation",
            name="backer_name",
            field=models.CharField(max_length=255),
        ),
    ]
