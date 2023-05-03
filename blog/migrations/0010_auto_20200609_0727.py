# Generated by Django 3.0.7 on 2020-06-09 07:27

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200608_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'strikethrough', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'blockquote'])), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(help_text='Paste a link to a video, audio file, instagram, etc.', icon='media', label='Embed media')), ('image_carousel', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.blocks.TextBlock(required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(required=False))]), icon='image', template='blog/blocks/carousel.html')), ('button', wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock(blank=True)), ('button_url', wagtail.blocks.URLBlock(label='Button link'))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body_de',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'strikethrough', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'blockquote'])), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(help_text='Paste a link to a video, audio file, instagram, etc.', icon='media', label='Embed media')), ('image_carousel', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.blocks.TextBlock(required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(required=False))]), icon='image', template='blog/blocks/carousel.html')), ('button', wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock(blank=True)), ('button_url', wagtail.blocks.URLBlock(label='Button link'))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body_en',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'strikethrough', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'blockquote'])), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(help_text='Paste a link to a video, audio file, instagram, etc.', icon='media', label='Embed media')), ('image_carousel', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.blocks.TextBlock(required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(required=False))]), icon='image', template='blog/blocks/carousel.html')), ('button', wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock(blank=True)), ('button_url', wagtail.blocks.URLBlock(label='Button link'))]))], blank=True, null=True),
        ),
    ]
