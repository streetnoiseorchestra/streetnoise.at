# Generated by Django 2.2.1 on 2019-05-06 09:32

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailimages', '0001_squashed_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='GigPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('gigomatic_id', models.CharField(max_length=255, null=True)),
                ('date_from', models.DateField(verbose_name='Start date')),
                ('date_to', models.DateField(blank=True, help_text='Not required if gig is on a single day', null=True, verbose_name='End date')),
                ('call_time', models.TimeField(blank=True, null=True, verbose_name='Set time')),
                ('set_time', models.TimeField(blank=True, null=True, verbose_name='Set time')),
                ('end_time', models.TimeField(blank=True, null=True, verbose_name='End time')),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('partner', models.CharField(blank=True, help_text="The organization we're doing the gig for", max_length=255, null=True)),
                ('link', models.URLField(blank=True)),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
                ('feed_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='GigIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
                ('feed_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
