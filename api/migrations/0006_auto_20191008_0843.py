# Generated by Django 2.2.6 on 2019-10-08 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20191007_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anketatest',
            name='personal',
        ),
        migrations.AddField(
            model_name='anketatest',
            name='personal1',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='anketatest',
            name='personal2',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='anketatest',
            name='personal3',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='anketatest',
            name='personal4',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='route',
            name='personal1',
            field=models.BooleanField(null=True, verbose_name='горы'),
        ),
        migrations.AddField(
            model_name='route',
            name='personal2',
            field=models.BooleanField(null=True, verbose_name='море'),
        ),
        migrations.AddField(
            model_name='route',
            name='personal3',
            field=models.BooleanField(null=True, verbose_name='город'),
        ),
        migrations.AddField(
            model_name='route',
            name='personal4',
            field=models.BooleanField(null=True, verbose_name='лес'),
        ),
    ]
