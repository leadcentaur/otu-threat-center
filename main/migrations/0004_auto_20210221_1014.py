# Generated by Django 3.1.5 on 2021-02-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210221_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportimages',
            name='image',
        ),
        migrations.AddField(
            model_name='reportimages',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
