# Generated by Django 2.2.6 on 2019-10-06 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnketaTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.BooleanField()),
                ('invalid', models.BooleanField()),
                ('invalid2', models.BooleanField()),
                ('age', models.IntegerField()),
                ('personal', models.CharField(max_length=20, null=True)),
                ('physReady', models.CharField(max_length=20, null=True)),
                ('Time', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('description', models.TextField(max_length=1000, verbose_name='описание')),
                ('difficulty', models.IntegerField(choices=[(1, 'Лёгкий'), (2, 'Средний'), (3, 'Сложный')], verbose_name='сложность')),
                ('duration', models.IntegerField(verbose_name='длительность')),
                ('image', models.FileField(default=b'', upload_to='', verbose_name='изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=100000, verbose_name='текст отзыва')),
            ],
        ),
    ]