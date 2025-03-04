# Generated by Django 5.1.3 on 2024-11-21 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_rename_slug_course_slug_field'),
        ('states', '0004_remove_localities_state_localities_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='localities',
            field=models.ManyToManyField(related_name='courses', to='states.localities'),
        ),
    ]
