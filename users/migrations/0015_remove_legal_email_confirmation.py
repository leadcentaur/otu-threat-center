# Generated by Django 3.1.5 on 2021-04-01 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20210331_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='legal',
            name='email_confirmation',
        ),
    ]
