# Generated by Django 2.2.12 on 2020-04-24 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0002_auto_20200424_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='is verified'),
        ),
    ]
