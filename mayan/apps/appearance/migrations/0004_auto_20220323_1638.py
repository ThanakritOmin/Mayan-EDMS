# Generated by Django 2.2.24 on 2022-03-23 16:38

import colorful.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0003_auto_20210823_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='background_color_header',
            field=colorful.fields.RGBColorField(blank=True, help_text='Color background header.', verbose_name='Color background header'),
        ),
        migrations.AddField(
            model_name='theme',
            name='background_color_header_panel',
            field=colorful.fields.RGBColorField(blank=True, help_text='Color background header panel.', verbose_name='Color background header panel'),
        ),
        migrations.AddField(
            model_name='theme',
            name='background_color_menu',
            field=colorful.fields.RGBColorField(blank=True, help_text='Color background menu.', verbose_name='Color background menu'),
        ),
        migrations.AddField(
            model_name='theme',
            name='background_menu_dropdown',
            field=colorful.fields.RGBColorField(blank=True, help_text='Color background dropdown menu.', verbose_name='Color background dropdown menu'),
        ),
        migrations.AddField(
            model_name='theme',
            name='background_website',
            field=colorful.fields.RGBColorField(blank=True, help_text='Color background website.', verbose_name='Color background website'),
        ),
        migrations.AddField(
            model_name='theme',
            name='btn_color_danger',
            field=colorful.fields.RGBColorField(blank=True, help_text='Color danger button.', verbose_name='Color danger button'),
        ),
        migrations.AddField(
            model_name='theme',
            name='btn_color_default',
            field=colorful.fields.RGBColorField(blank=True, help_text='Color default button.', verbose_name='Color default button'),
        ),
        migrations.AddField(
            model_name='theme',
            name='btn_color_primary',
            field=colorful.fields.RGBColorField(blank=True, help_text='Color primary button.', verbose_name='Color primary button'),
        ),
        migrations.AddField(
            model_name='theme',
            name='btn_color_success',
            field=colorful.fields.RGBColorField(blank=True, help_text='Color success button.', verbose_name='Color success button'),
        ),
        migrations.AddField(
            model_name='theme',
            name='color_font_header',
            field=colorful.fields.RGBColorField(blank=True, help_text='Color font title and all content.', verbose_name='Color font title Color font title and all content.'),
        ),
        migrations.AddField(
            model_name='theme',
            name='font',
            field=models.CharField(blank=True, choices=[('Kanit', 'Kanit font'), ('Roboto', 'Roboto font'), ('Prompt', 'Prompt font')], max_length=100, verbose_name='Font'),
        ),
        migrations.AddField(
            model_name='theme',
            name='font_size_content_title',
            field=models.IntegerField(default=23, help_text='Font size content title.', verbose_name='Font size content title'),
        ),
        migrations.AddField(
            model_name='theme',
            name='font_size_header',
            field=models.IntegerField(default=19, help_text='Font size header brand.', verbose_name='Font size brand'),
        ),
        migrations.AddField(
            model_name='theme',
            name='font_size_menu',
            field=models.IntegerField(default=15, help_text='Font size menu.', verbose_name='Font size menu'),
        ),
        migrations.AddField(
            model_name='theme',
            name='menu_text_color',
            field=colorful.fields.RGBColorField(blank=True, help_text='Menu text color.', verbose_name='Menu text color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='label',
            field=models.CharField(db_index=True, max_length=128, unique=True, verbose_name='ชื่อธีม'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='stylesheet',
            field=models.TextField(blank=True, verbose_name='Stylesheet'),
        ),
    ]
