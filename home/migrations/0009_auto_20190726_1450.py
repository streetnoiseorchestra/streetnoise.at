# Generated by Django 2.2.3 on 2019-07-26 14:50

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_genericpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericpage',
            name='content',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('rawhtml', wagtail.blocks.RawHTMLBlock()), ('quote', wagtail.blocks.BlockQuoteBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('imagetile', wagtail.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='content_de',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('rawhtml', wagtail.blocks.RawHTMLBlock()), ('quote', wagtail.blocks.BlockQuoteBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('imagetile', wagtail.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='content_en',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('rawhtml', wagtail.blocks.RawHTMLBlock()), ('quote', wagtail.blocks.BlockQuoteBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('imagetile', wagtail.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())]))], blank=True, null=True),
        ),
    ]
