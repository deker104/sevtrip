from datetime import datetime

from django.db import models


class Route(models.Model):
    DIFFICULTY_CHOICES = [
        (1, 'Лёгкий'),
        (2, 'Средний'),
        (3, 'Сложный')
    ]
    name = models.CharField('название', max_length=100)
    description = models.TextField('описание', max_length=1000)
    difficulty = models.IntegerField('сложность', choices=DIFFICULTY_CHOICES)
    html = models.TextField('карта', max_length=10000, blank=True)
    image = models.FileField('изображение', default='')
    personal1 = models.BooleanField('горы', null=True)
    personal2 = models.BooleanField('море', null=True)
    personal3 = models.BooleanField('город', null=True)
    personal4 = models.BooleanField('лес', null=True)


class Suggestion(models.Model):
    text = models.TextField('текст отзыва', max_length=100000)


class AnketaTest(models.Model):
    child = models.BooleanField()
    invalid = models.BooleanField()
    invalid2 = models.BooleanField()
    age = models.IntegerField()
    personal1 = models.BooleanField(null=True)
    personal2 = models.BooleanField(null=True)
    personal3 = models.BooleanField(null=True)
    personal4 = models.BooleanField(null=True)
    physReady = models.IntegerField(null=True)
    Time = models.IntegerField(null=True)
