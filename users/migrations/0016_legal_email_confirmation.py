# Generated by Django 3.1.5 on 2021-04-01 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_remove_legal_email_confirmation'),
    ]

    operations = [
        migrations.AddField(
            model_name='legal',
            name='email_confirmation',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
