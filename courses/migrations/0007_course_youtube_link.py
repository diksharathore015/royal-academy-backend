# Generated by Django 5.1.3 on 2024-11-13 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_course_contact_number_course_facebook_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='youtube_link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
