# Generated by Django 4.0.8 on 2023-05-01 10:07

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_rename_home_page_homepagebandfriend_homepage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericpage',
            name='content',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'strikethrough', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'blockquote'])), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('rawhtml', wagtail.blocks.RawHTMLBlock()), ('quote', wagtail.blocks.BlockQuoteBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock(help_text='Paste a link to a video, audio file, instagram, etc.', icon='media', label='Embed media')), ('imagetile', wagtail.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())])), ('imagetile2', wagtail.blocks.StructBlock([('aspect_ratio', wagtail.blocks.ChoiceBlock(choices=[('', 'Select Aspect Ratio of Images'), ('1:1', '1:1 Square'), ('1:1 sm', '1:1 Square (smaller)'), ('3:2', '3:2'), ('4:3', '4:3 (traditional)'), ('16:9', '16:9 (widescreen)')])), ('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.TextBlock(required=False)), ('attribution', wagtail.blocks.TextBlock(required=False, verbose_name='Photographer Credit')), ('attribution_url', wagtail.blocks.URLBlock(required=False, vervose_name='Photographer URL'))]), icon='image'))])), ('footercta', wagtail.blocks.StructBlock([('cta_title', wagtail.blocks.CharBlock(blank=True, verbose_name='CTA Title')), ('cta_subtitle', wagtail.blocks.CharBlock(blank=True, verbose_name='CTA Subtitle')), ('cta_button1', wagtail.blocks.CharBlock(blank=True, verbose_name='Button 1 Text')), ('cta_button2', wagtail.blocks.CharBlock(blank=True, verbose_name='Button 2 Text')), ('cta_button1_url', wagtail.blocks.URLBlock(form_classname='full title')), ('cta_button2_url', wagtail.blocks.URLBlock(form_classname='full title'))])), ('newsletter_signup', wagtail.blocks.StructBlock([('cta_title', wagtail.blocks.CharBlock(blank=True, verbose_name='Title')), ('cta_subtitle', wagtail.blocks.CharBlock(blank=True, verbose_name='Subtitle')), ('newsletter_type', wagtail.blocks.ChoiceBlock(choices=[('', 'Select Type of Newsletter'), ('generic-newsletter', 'Generic'), ('festival-newsletter', 'Festival (Green)')]))])), ('image_grid', wagtail.blocks.StructBlock([('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.TextBlock(required=False)), ('attribution', wagtail.blocks.TextBlock(required=False, verbose_name='Photographer Credit')), ('attribution_url', wagtail.blocks.URLBlock(required=False, vervose_name='Photographer URL'))]), icon='image', template='home/blocks/image_grid.html'))])), ('paragraph_image', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(group='Image', required=True)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('', 'Select Image alignment'), ('left', 'Image Left'), ('right', 'Image Right')], group='Image')), ('with_shadow', wagtail.blocks.BooleanBlock(default=True, group='Image', help_text='Add a shadow to the image, good for photographs')), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('', 'Section Background Color'), ('green', 'SNO Green'), ('orange', 'SNO Orange'), ('blue', 'Blue'), ('white', 'White')])), ('body', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'strikethrough', 'ol', 'ul', 'hr', 'link', 'document-link', 'blockquote'], required=True))]))], blank=True, null=True, use_json_field=None),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='content_de',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'strikethrough', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'blockquote'])), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('rawhtml', wagtail.blocks.RawHTMLBlock()), ('quote', wagtail.blocks.BlockQuoteBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock(help_text='Paste a link to a video, audio file, instagram, etc.', icon='media', label='Embed media')), ('imagetile', wagtail.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())])), ('imagetile2', wagtail.blocks.StructBlock([('aspect_ratio', wagtail.blocks.ChoiceBlock(choices=[('', 'Select Aspect Ratio of Images'), ('1:1', '1:1 Square'), ('1:1 sm', '1:1 Square (smaller)'), ('3:2', '3:2'), ('4:3', '4:3 (traditional)'), ('16:9', '16:9 (widescreen)')])), ('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.TextBlock(required=False)), ('attribution', wagtail.blocks.TextBlock(required=False, verbose_name='Photographer Credit')), ('attribution_url', wagtail.blocks.URLBlock(required=False, vervose_name='Photographer URL'))]), icon='image'))])), ('footercta', wagtail.blocks.StructBlock([('cta_title', wagtail.blocks.CharBlock(blank=True, verbose_name='CTA Title')), ('cta_subtitle', wagtail.blocks.CharBlock(blank=True, verbose_name='CTA Subtitle')), ('cta_button1', wagtail.blocks.CharBlock(blank=True, verbose_name='Button 1 Text')), ('cta_button2', wagtail.blocks.CharBlock(blank=True, verbose_name='Button 2 Text')), ('cta_button1_url', wagtail.blocks.URLBlock(form_classname='full title')), ('cta_button2_url', wagtail.blocks.URLBlock(form_classname='full title'))])), ('newsletter_signup', wagtail.blocks.StructBlock([('cta_title', wagtail.blocks.CharBlock(blank=True, verbose_name='Title')), ('cta_subtitle', wagtail.blocks.CharBlock(blank=True, verbose_name='Subtitle')), ('newsletter_type', wagtail.blocks.ChoiceBlock(choices=[('', 'Select Type of Newsletter'), ('generic-newsletter', 'Generic'), ('festival-newsletter', 'Festival (Green)')]))])), ('image_grid', wagtail.blocks.StructBlock([('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.TextBlock(required=False)), ('attribution', wagtail.blocks.TextBlock(required=False, verbose_name='Photographer Credit')), ('attribution_url', wagtail.blocks.URLBlock(required=False, vervose_name='Photographer URL'))]), icon='image', template='home/blocks/image_grid.html'))])), ('paragraph_image', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(group='Image', required=True)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('', 'Select Image alignment'), ('left', 'Image Left'), ('right', 'Image Right')], group='Image')), ('with_shadow', wagtail.blocks.BooleanBlock(default=True, group='Image', help_text='Add a shadow to the image, good for photographs')), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('', 'Section Background Color'), ('green', 'SNO Green'), ('orange', 'SNO Orange'), ('blue', 'Blue'), ('white', 'White')])), ('body', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'strikethrough', 'ol', 'ul', 'hr', 'link', 'document-link', 'blockquote'], required=True))]))], blank=True, null=True, use_json_field=None),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='content_en',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'strikethrough', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'blockquote'])), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('rawhtml', wagtail.blocks.RawHTMLBlock()), ('quote', wagtail.blocks.BlockQuoteBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock(help_text='Paste a link to a video, audio file, instagram, etc.', icon='media', label='Embed media')), ('imagetile', wagtail.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())])), ('imagetile2', wagtail.blocks.StructBlock([('aspect_ratio', wagtail.blocks.ChoiceBlock(choices=[('', 'Select Aspect Ratio of Images'), ('1:1', '1:1 Square'), ('1:1 sm', '1:1 Square (smaller)'), ('3:2', '3:2'), ('4:3', '4:3 (traditional)'), ('16:9', '16:9 (widescreen)')])), ('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.TextBlock(required=False)), ('attribution', wagtail.blocks.TextBlock(required=False, verbose_name='Photographer Credit')), ('attribution_url', wagtail.blocks.URLBlock(required=False, vervose_name='Photographer URL'))]), icon='image'))])), ('footercta', wagtail.blocks.StructBlock([('cta_title', wagtail.blocks.CharBlock(blank=True, verbose_name='CTA Title')), ('cta_subtitle', wagtail.blocks.CharBlock(blank=True, verbose_name='CTA Subtitle')), ('cta_button1', wagtail.blocks.CharBlock(blank=True, verbose_name='Button 1 Text')), ('cta_button2', wagtail.blocks.CharBlock(blank=True, verbose_name='Button 2 Text')), ('cta_button1_url', wagtail.blocks.URLBlock(form_classname='full title')), ('cta_button2_url', wagtail.blocks.URLBlock(form_classname='full title'))])), ('newsletter_signup', wagtail.blocks.StructBlock([('cta_title', wagtail.blocks.CharBlock(blank=True, verbose_name='Title')), ('cta_subtitle', wagtail.blocks.CharBlock(blank=True, verbose_name='Subtitle')), ('newsletter_type', wagtail.blocks.ChoiceBlock(choices=[('', 'Select Type of Newsletter'), ('generic-newsletter', 'Generic'), ('festival-newsletter', 'Festival (Green)')]))])), ('image_grid', wagtail.blocks.StructBlock([('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.TextBlock(required=False)), ('attribution', wagtail.blocks.TextBlock(required=False, verbose_name='Photographer Credit')), ('attribution_url', wagtail.blocks.URLBlock(required=False, vervose_name='Photographer URL'))]), icon='image', template='home/blocks/image_grid.html'))])), ('paragraph_image', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(group='Image', required=True)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('', 'Select Image alignment'), ('left', 'Image Left'), ('right', 'Image Right')], group='Image')), ('with_shadow', wagtail.blocks.BooleanBlock(default=True, group='Image', help_text='Add a shadow to the image, good for photographs')), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('', 'Section Background Color'), ('green', 'SNO Green'), ('orange', 'SNO Orange'), ('blue', 'Blue'), ('white', 'White')])), ('body', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'strikethrough', 'ol', 'ul', 'hr', 'link', 'document-link', 'blockquote'], required=True))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
