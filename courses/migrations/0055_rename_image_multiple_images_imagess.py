# Generated by Django 5.0 on 2024-12-26 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "courses",
            "0054_remove_multiple_images_imagess_multiple_images_image_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="multiple_images", old_name="image", new_name="imagess",
        ),
    ]
