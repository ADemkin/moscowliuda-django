from django.db import models

from project.models import Project


class TextBook(models.Model):
    title = models.CharField(verbose_name='Заголовок',max_length=100)
    sub_title = models.CharField(verbose_name='Подзаголовок',max_length=100)
    price_rub = models.IntegerField(verbose_name='Цена')
    main_photo = models.ImageField(verbose_name='Главное Фото')
    description = models.TextField(verbose_name='Описание', max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")


class TextBookPhoto(models.Model):
    photo = models.ImageField(upload_to='text_book_photos')
    book = models.ForeignKey(TextBook, on_delete=models.CASCADE, related_name='photos', verbose_name='Пособие')


class YoutubeUrl(models.Model):
    url = models.URLField()
    books = models.ManyToManyField(TextBook, related_name='youtube_urls', verbose_name='Пособия')
    projects = models.ManyToManyField(Project, related_name='youtube_urls', verbose_name='Проекты')
