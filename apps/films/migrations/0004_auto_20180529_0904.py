# Generated by Django 2.0.1 on 2018-05-29 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_auto_20180528_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='intro',
            field=models.TextField(default='', max_length=800, verbose_name='电影介绍'),
        ),
    ]