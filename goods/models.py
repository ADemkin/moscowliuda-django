from django.db import models


class Photo(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название фото')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фото')

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


class Good(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    sub_title = models.CharField(verbose_name='Подзаголовок', max_length=100)
    price_rub = models.IntegerField(verbose_name='Цена')
    main_photo = models.ImageField(null=True, verbose_name='Главное фото', related_name='main_photo_of')
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
    main_photo = models.OneToOneField(
        Photo,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Главное фото',
        related_name='main_photo_of_project'
    )

    description = models.TextField(verbose_name='Описание', max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    urls = models.ManyToManyField(
        Url,
        verbose_name='Ссылки на ютуб',
        related_name='projects',
        blank=True
    )
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
