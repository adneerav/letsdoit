# Generated by Django 2.2.12 on 2020-04-25 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200425_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='genres',
            field=models.ManyToManyField(related_name='contents', related_query_name='content', to='movies.Genre'),
        ),
    ]