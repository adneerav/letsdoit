# Generated by Django 2.2.12 on 2020-04-25 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0004_auto_20200425_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=500, verbose_name='password'),
        ),
    ]
