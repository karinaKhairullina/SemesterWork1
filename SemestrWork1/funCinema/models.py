from django.db import models
from audioop import reverse

from django.db import models


class Category(models.Model):
    name = models.CharField("Категория", max_length= 100)
    description = models.TextField("Описание", max_length=500)
    url = models.SlugField(unique=False)

    def __str__(self):
        return self.name


class Actor(models.Model):
    FIO = models.CharField('ФИО', max_length= 100)
    age = models.IntegerField(default=0)
    description = models.TextField('Описание', max_length=500)
    image = models.ImageField(upload_to='actors/')

    def __str__(self):
        return self.FIO


class Genre(models.Model):
    name = models.CharField(max_length=100)
    url = models.SlugField(unique=False)

    def __str__(self):
        return self.name


class Serials(models.Model):
    title = models.CharField('Название',max_length=100)
    description = models.CharField('Описание', max_length= 200)
    poster = models.ImageField('Постер', upload_to='serials/')
    date = models.DateField('Дата выхода', null=True)
    country = models.CharField('Страна',max_length=100)
    actors = models.ManyToManyField(Actor, verbose_name='актеры', related_name='actor')   # использование M2M
    # related name позволяет запрашивать связанные сущности из бд
    genre = models.ManyToManyField(Genre, verbose_name='жанры')  # использование M2M
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.SET_NULL, null=True)    # использование O2M
    #если удалим категорию, то поле = 0
    url = models.SlugField(unique=False)
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):   # возвращает удобочитаемую строку для названия
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Сериал'
        verbose_name_plural = 'Сериалы'

class Cadrs(models.Model):
    name = models.CharField('Заголовок', max_length= 100)
    image = models.ImageField()
    serial = models.ForeignKey(Serials, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
