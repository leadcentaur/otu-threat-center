# Generated by Django 3.1.5 on 2021-04-11 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vpnuser',
            name='vpn_password',
            field=models.CharField(max_length=12),
        ),
    ]
