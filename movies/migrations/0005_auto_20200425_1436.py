# Generated by Django 2.2.12 on 2020-04-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20200425_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='genre'),
        ),
    ]