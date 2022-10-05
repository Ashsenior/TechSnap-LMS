# Generated by Django 3.2.6 on 2022-09-24 11:22

import course.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.CharField(default=course.models.generate_profile_code, max_length=50),
        ),
    ]
