# Generated by Django 3.1.5 on 2021-04-01 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210331_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legal',
            name='email_confirmation',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]