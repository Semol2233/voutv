# Generated by Django 2.2.5 on 2020-05-24 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_app', '0007_auto_20200524_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcreate',
            name='contentlink',
            field=models.URLField(blank=True, default='http://www.jagobd.com/makkahlive'),
        ),
    ]
