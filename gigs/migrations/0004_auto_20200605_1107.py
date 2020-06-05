# Generated by Django 3.0.7 on 2020-06-05 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gigs', '0003_auto_20200605_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gigpage',
            name='link',
            field=models.URLField(blank=True, help_text='A link to a blog, facebook page, or other site about this gig.'),
        ),
        migrations.AlterField(
            model_name='gigpage',
            name='location',
            field=models.CharField(blank=True, help_text='Where is the gig taking place?', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='gigpage',
            name='partner',
            field=models.CharField(blank=True, help_text='Which organization are we doing the gig with?', max_length=255, null=True),
        ),
    ]
