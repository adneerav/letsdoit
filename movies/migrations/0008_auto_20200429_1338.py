# Generated by Django 2.2.12 on 2020-04-29 13:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20200429_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='added_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]