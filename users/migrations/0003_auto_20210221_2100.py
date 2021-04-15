# Generated by Django 3.1.5 on 2021-02-22 02:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210221_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics', validators=[django.core.validators.validate_image_file_extension]),
        ),
    ]
