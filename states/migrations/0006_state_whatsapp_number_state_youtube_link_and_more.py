# Generated by Django 5.0 on 2025-01-09 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("states", "0005_cities_youtube_link_alter_cities_contact_number_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="state",
            name="Whatsapp_number",
            field=models.CharField(
                blank=True, default="8278640248", max_length=100, null=True
            ),
        ),
        migrations.AddField(
            model_name="state",
            name="youtube_link",
            field=models.CharField(
                blank=True,
                default="https://www.youtube.com/@rdajaipur",
                max_length=250,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="state",
            name="contact_number",
            field=models.CharField(
                blank=True, default="8619453001", max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="state",
            name="facebook_link",
            field=models.CharField(
                blank=True,
                default="https://www.facebook.com/Sainikschoolentranceexamcoaching/",
                max_length=250,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="state",
            name="instagram_link",
            field=models.CharField(
                blank=True,
                default="https://www.instagram.com/onlinesainikschoolcoaching/",
                max_length=250,
                null=True,
            ),
        ),
    ]
