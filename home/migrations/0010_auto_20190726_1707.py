# Generated by Django 2.2.3 on 2019-07-26 17:07

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190726_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericpage',
            name='content',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('rawhtml', wagtail.core.blocks.RawHTMLBlock()), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('imagetile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())])), ('footercta', wagtail.core.blocks.StructBlock([('cta_title', wagtail.core.blocks.CharBlock(blank=True, verbose_name='CTA Title')), ('cta_subtitle', wagtail.core.blocks.CharBlock(blank=True, verbose_name='CTA Subtitle')), ('cta_button1', wagtail.core.blocks.CharBlock(blank=True, verbose_name='Button 1 Text')), ('cta_button2', wagtail.core.blocks.CharBlock(blank=True, verbose_name='Button 2 Text')), ('cta_button1_url', wagtail.core.blocks.URLBlock(classname='full title')), ('cta_button2_url', wagtail.core.blocks.URLBlock(classname='full title'))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='content_de',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('rawhtml', wagtail.core.blocks.RawHTMLBlock()), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('imagetile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())])), ('footercta', wagtail.core.blocks.StructBlock([('cta_title', wagtail.core.blocks.CharBlock(blank=True, verbose_name='CTA Title')), ('cta_subtitle', wagtail.core.blocks.CharBlock(blank=True, verbose_name='CTA Subtitle')), ('cta_button1', wagtail.core.blocks.CharBlock(blank=True, verbose_name='Button 1 Text')), ('cta_button2', wagtail.core.blocks.CharBlock(blank=True, verbose_name='Button 2 Text')), ('cta_button1_url', wagtail.core.blocks.URLBlock(classname='full title')), ('cta_button2_url', wagtail.core.blocks.URLBlock(classname='full title'))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='content_en',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('rawhtml', wagtail.core.blocks.RawHTMLBlock()), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('imagetile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())])), ('footercta', wagtail.core.blocks.StructBlock([('cta_title', wagtail.core.blocks.CharBlock(blank=True, verbose_name='CTA Title')), ('cta_subtitle', wagtail.core.blocks.CharBlock(blank=True, verbose_name='CTA Subtitle')), ('cta_button1', wagtail.core.blocks.CharBlock(blank=True, verbose_name='Button 1 Text')), ('cta_button2', wagtail.core.blocks.CharBlock(blank=True, verbose_name='Button 2 Text')), ('cta_button1_url', wagtail.core.blocks.URLBlock(classname='full title')), ('cta_button2_url', wagtail.core.blocks.URLBlock(classname='full title'))]))], blank=True, null=True),
        ),
    ]
