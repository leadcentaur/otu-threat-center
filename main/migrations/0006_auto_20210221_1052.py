# Generated by Django 3.1.5 on 2021-02-21 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210221_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='img_a',
            field=models.ImageField(default='default.jpg', upload_to='report_pics'),
        ),
        migrations.AddField(
            model_name='report',
            name='img_b',
            field=models.ImageField(default='default.jpg', upload_to='report_pics'),
        ),
        migrations.DeleteModel(
            name='ReportImages',
        ),
    ]
