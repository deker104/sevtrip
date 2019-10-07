# Generated by Django 2.2.6 on 2019-10-07 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191006_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='html',
            field=models.CharField(blank=True, max_length=10000, verbose_name='карта'),
        ),
        migrations.AddField(
            model_name='route',
            name='image',
            field=models.FileField(default='', upload_to='', verbose_name='изображение'),
        ),
    ]
