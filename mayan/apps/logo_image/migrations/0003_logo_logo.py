# Generated by Django 2.2.24 on 2022-03-02 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logo_image', '0002_auto_20220226_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo',
            name='logo',
            field=models.ImageField(default=None, upload_to='logo'),
        ),
    ]