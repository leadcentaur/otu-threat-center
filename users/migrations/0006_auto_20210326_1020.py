# Generated by Django 3.1.5 on 2021-03-26 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210326_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='legal',
        ),
        migrations.DeleteModel(
            name='Legal',
        ),
    ]
