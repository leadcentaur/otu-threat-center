# Generated by Django 3.1.5 on 2021-04-11 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20210411_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legal',
            name='email_confirmation',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=42, null=True),
        ),
    ]
