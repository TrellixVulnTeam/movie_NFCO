# Generated by Django 2.0.1 on 2018-05-10 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_auto_20180510_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='image/movie/default.png', upload_to='image/movie/%Y/%m', verbose_name='电影图'),
        ),
    ]
