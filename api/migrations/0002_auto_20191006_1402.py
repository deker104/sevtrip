# Generated by Django 2.2.6 on 2019-10-06 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='route',
            name='image',
        ),
    ]
