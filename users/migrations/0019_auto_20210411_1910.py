# Generated by Django 3.1.5 on 2021-04-11 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20210411_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legal',
            name='email_confirmation',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=42),
        ),
    ]
