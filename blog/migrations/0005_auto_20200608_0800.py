# Generated by Django 3.0.7 on 2020-06-08 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200604_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='extra_css',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='hide_author',
            field=models.BooleanField(default=False, help_text='Hide the author sign-off.'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='hide_header_overlay',
            field=models.BooleanField(default=False, help_text='Do not apply the subtle color overlay to the header image on the blog post page.'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='hide_header_title',
            field=models.BooleanField(default=False, help_text='Hide the blog title from the header image on the blog post page.'),
        ),
    ]