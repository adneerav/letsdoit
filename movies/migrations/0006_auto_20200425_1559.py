# Generated by Django 2.2.12 on 2020-04-25 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20200425_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=50, verbose_name='genre'),
        ),
    ]
