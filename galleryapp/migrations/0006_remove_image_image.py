# Generated by Django 3.2.8 on 2021-10-11 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleryapp', '0005_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
    ]