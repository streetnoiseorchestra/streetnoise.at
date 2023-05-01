# Generated by Django 4.0.8 on 2023-05-01 10:07

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('festival2023', '0005_alter_festivalpage2023_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festivalpage2023',
            name='body',
            field=wagtail.fields.StreamField([('heading_text', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('text', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'strikethrough', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'blockquote']))])), ('paragraph_image', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(group='Image', required=True)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('', 'Select Image alignment'), ('left', 'Image Left'), ('right', 'Image Right')], group='Image')), ('with_shadow', wagtail.blocks.BooleanBlock(default=True, group='Image', help_text='Add a shadow to the image, good for photographs')), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('', 'Section Background Color'), ('green', 'SNO Green'), ('orange', 'SNO Orange'), ('blue', 'Blue'), ('white', 'White')])), ('body', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'strikethrough', 'ol', 'ul', 'hr', 'link', 'document-link', 'blockquote'], required=True))])), ('image_grid', wagtail.blocks.StructBlock([('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.TextBlock(required=False)), ('attribution', wagtail.blocks.TextBlock(required=False, verbose_name='Photographer Credit')), ('attribution_url', wagtail.blocks.URLBlock(required=False, vervose_name='Photographer URL'))]), icon='image', template='home/blocks/image_grid.html'))])), ('number_boxes', wagtail.blocks.StructBlock([('boxes', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('value', wagtail.blocks.CharBlock(max_length=40, required=True)), ('label', wagtail.blocks.TextBlock(max_length=200, required=True))])))])), ('lineup', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('performers', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(max_length=255, required=True)), ('location', wagtail.blocks.CharBlock(max_length=255, required=True)), ('website', wagtail.blocks.URLBlock(required=False)), ('social', wagtail.blocks.URLBlock(required=False)), ('logo', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('funders', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('funders', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(max_length=255, required=True)), ('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.blocks.URLBlock(required=False))])))], label='Funders & Sponsors')), ('program2', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(label='Program Section Heading')), ('timeline', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock())], label='Timeline Item Name')), ('item', wagtail.blocks.StructBlock([('icon', wagtail.blocks.CharBlock()), ('title', wagtail.blocks.CharBlock(label='Time')), ('detail', wagtail.blocks.CharBlock(label='Name')), ('small_detail', wagtail.blocks.CharBlock(label='Extra Detail', required=False))], label='Timeline Item Info'))], label='Program Timeline Items')), ('descriptions', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.CharBlock(form_classname='full title', label='Program Item Heading')), ('item', wagtail.blocks.RichTextBlock(label='Program Item Description'))], label='Program Descriptions'))], label='Program')), ('newsletter', wagtail.blocks.StructBlock([('cta_title', wagtail.blocks.CharBlock(blank=True, verbose_name='Title')), ('cta_subtitle', wagtail.blocks.CharBlock(blank=True, verbose_name='Subtitle')), ('newsletter_type', wagtail.blocks.ChoiceBlock(choices=[('', 'Select Type of Newsletter'), ('generic-newsletter', 'Generic'), ('festival-newsletter', 'Festival (Green)')]))])), ('embed', wagtail.embeds.blocks.EmbedBlock(help_text='Paste a link to a video, audio file, instagram, etc.', icon='media', label='Embed media'))], blank=True, null=True, use_json_field=None),
        ),
        migrations.AlterField(
            model_name='festivalpage2023',
            name='body_de',
            field=wagtail.fields.StreamField([('heading_text', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('text', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'strikethrough', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'blockquote']))])), ('paragraph_image', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(group='Image', required=True)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('', 'Select Image alignment'), ('left', 'Image Left'), ('right', 'Image Right')], group='Image')), ('with_shadow', wagtail.blocks.BooleanBlock(default=True, group='Image', help_text='Add a shadow to the image, good for photographs')), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('', 'Section Background Color'), ('green', 'SNO Green'), ('orange', 'SNO Orange'), ('blue', 'Blue'), ('white', 'White')])), ('body', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'strikethrough', 'ol', 'ul', 'hr', 'link', 'document-link', 'blockquote'], required=True))])), ('image_grid', wagtail.blocks.StructBlock([('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.TextBlock(required=False)), ('attribution', wagtail.blocks.TextBlock(required=False, verbose_name='Photographer Credit')), ('attribution_url', wagtail.blocks.URLBlock(required=False, vervose_name='Photographer URL'))]), icon='image', template='home/blocks/image_grid.html'))])), ('number_boxes', wagtail.blocks.StructBlock([('boxes', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('value', wagtail.blocks.CharBlock(max_length=40, required=True)), ('label', wagtail.blocks.TextBlock(max_length=200, required=True))])))])), ('lineup', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('performers', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(max_length=255, required=True)), ('location', wagtail.blocks.CharBlock(max_length=255, required=True)), ('website', wagtail.blocks.URLBlock(required=False)), ('social', wagtail.blocks.URLBlock(required=False)), ('logo', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('funders', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('funders', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(max_length=255, required=True)), ('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.blocks.URLBlock(required=False))])))], label='Funders & Sponsors')), ('program2', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(label='Program Section Heading')), ('timeline', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock())], label='Timeline Item Name')), ('item', wagtail.blocks.StructBlock([('icon', wagtail.blocks.CharBlock()), ('title', wagtail.blocks.CharBlock(label='Time')), ('detail', wagtail.blocks.CharBlock(label='Name')), ('small_detail', wagtail.blocks.CharBlock(label='Extra Detail', required=False))], label='Timeline Item Info'))], label='Program Timeline Items')), ('descriptions', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.CharBlock(form_classname='full title', label='Program Item Heading')), ('item', wagtail.blocks.RichTextBlock(label='Program Item Description'))], label='Program Descriptions'))], label='Program')), ('newsletter', wagtail.blocks.StructBlock([('cta_title', wagtail.blocks.CharBlock(blank=True, verbose_name='Title')), ('cta_subtitle', wagtail.blocks.CharBlock(blank=True, verbose_name='Subtitle')), ('newsletter_type', wagtail.blocks.ChoiceBlock(choices=[('', 'Select Type of Newsletter'), ('generic-newsletter', 'Generic'), ('festival-newsletter', 'Festival (Green)')]))])), ('embed', wagtail.embeds.blocks.EmbedBlock(help_text='Paste a link to a video, audio file, instagram, etc.', icon='media', label='Embed media'))], blank=True, null=True, use_json_field=None),
        ),
        migrations.AlterField(
            model_name='festivalpage2023',
            name='body_en',
            field=wagtail.fields.StreamField([('heading_text', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('text', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'strikethrough', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'blockquote']))])), ('paragraph_image', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(group='Image', required=True)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('', 'Select Image alignment'), ('left', 'Image Left'), ('right', 'Image Right')], group='Image')), ('with_shadow', wagtail.blocks.BooleanBlock(default=True, group='Image', help_text='Add a shadow to the image, good for photographs')), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('', 'Section Background Color'), ('green', 'SNO Green'), ('orange', 'SNO Orange'), ('blue', 'Blue'), ('white', 'White')])), ('body', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'strikethrough', 'ol', 'ul', 'hr', 'link', 'document-link', 'blockquote'], required=True))])), ('image_grid', wagtail.blocks.StructBlock([('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.TextBlock(required=False)), ('attribution', wagtail.blocks.TextBlock(required=False, verbose_name='Photographer Credit')), ('attribution_url', wagtail.blocks.URLBlock(required=False, vervose_name='Photographer URL'))]), icon='image', template='home/blocks/image_grid.html'))])), ('number_boxes', wagtail.blocks.StructBlock([('boxes', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('value', wagtail.blocks.CharBlock(max_length=40, required=True)), ('label', wagtail.blocks.TextBlock(max_length=200, required=True))])))])), ('lineup', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('performers', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(max_length=255, required=True)), ('location', wagtail.blocks.CharBlock(max_length=255, required=True)), ('website', wagtail.blocks.URLBlock(required=False)), ('social', wagtail.blocks.URLBlock(required=False)), ('logo', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('funders', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('funders', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(max_length=255, required=True)), ('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.blocks.URLBlock(required=False))])))], label='Funders & Sponsors')), ('program2', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(label='Program Section Heading')), ('timeline', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock())], label='Timeline Item Name')), ('item', wagtail.blocks.StructBlock([('icon', wagtail.blocks.CharBlock()), ('title', wagtail.blocks.CharBlock(label='Time')), ('detail', wagtail.blocks.CharBlock(label='Name')), ('small_detail', wagtail.blocks.CharBlock(label='Extra Detail', required=False))], label='Timeline Item Info'))], label='Program Timeline Items')), ('descriptions', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.CharBlock(form_classname='full title', label='Program Item Heading')), ('item', wagtail.blocks.RichTextBlock(label='Program Item Description'))], label='Program Descriptions'))], label='Program')), ('newsletter', wagtail.blocks.StructBlock([('cta_title', wagtail.blocks.CharBlock(blank=True, verbose_name='Title')), ('cta_subtitle', wagtail.blocks.CharBlock(blank=True, verbose_name='Subtitle')), ('newsletter_type', wagtail.blocks.ChoiceBlock(choices=[('', 'Select Type of Newsletter'), ('generic-newsletter', 'Generic'), ('festival-newsletter', 'Festival (Green)')]))])), ('embed', wagtail.embeds.blocks.EmbedBlock(help_text='Paste a link to a video, audio file, instagram, etc.', icon='media', label='Embed media'))], blank=True, null=True, use_json_field=None),
        ),
    ]
