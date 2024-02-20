import os
from uuid import uuid4
from django.db import models

def unique_file_name(filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid4()}.{ext}"
    return os.path.join('text_book_photos', filename)

class Photo(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название фото')
    photo = models.ImageField(upload_to=unique_file_name)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return f"{self.id} - {self.name}"


class Url(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        verbose_name = 'Ссылка на ютуб'
        verbose_name_plural = 'Ссылки на ютуб'


class TextBook(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    sub_title = models.CharField(verbose_name='Подзаголовок', max_length=100)
    price_rub = models.IntegerField(verbose_name='Цена')
    main_photo = models.OneToOneField(Photo, on_delete=models.SET_NULL, null=True, verbose_name='Главное фото',
                                      related_name='main_photo_of')
    secondary_photos = models.ManyToManyField(Photo, verbose_name='Второстепенные фото', related_name='text_books',
                                              blank=True)
    urls = models.ManyToManyField(Url, verbose_name='Ссылки на ютуб', related_name='text_books', blank=True)
    description = models.TextField(verbose_name='Описание', max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = 'Учебник'
        verbose_name_plural = 'Учебники'

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    sub_title = models.CharField(verbose_name='Подзаголовок', max_length=100)
    main_photo = models.ImageField(verbose_name='Главное Фото', upload_to='project_photos')
    description = models.TextField(verbose_name='Описание', max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    url = models.URLField(verbose_name='Ссылка на проект')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
