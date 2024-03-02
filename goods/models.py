from django.db import models


class Good(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    sub_title = models.CharField(verbose_name='Подзаголовок', max_length=100)
    price_rub = models.IntegerField(verbose_name='Цена')
    main_photo = models.ImageField(null=True, upload_to='photos/', verbose_name='Главное фото')
    description = models.TextField(verbose_name='Описание', max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = 'Пособие'
        verbose_name_plural = 'Пособия'

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    sub_title = models.CharField(verbose_name='Подзаголовок', max_length=100)
    main_photo = models.ImageField(null=True, upload_to='photos/', verbose_name='Главное фото')
    description = models.TextField(verbose_name='Описание', max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Photo(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название фото')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фото')
    good = models.ForeignKey(Good, null=True,blank=True, on_delete=models.CASCADE, verbose_name='Пособие',
                             related_name='good_photos')
    project = models.ForeignKey(Project, null=True,blank=True, on_delete=models.CASCADE, verbose_name='Проект',
                                related_name='project_photos')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return f"{self.id} - {self.name}"


class Url(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    good = models.ForeignKey(Good, null=True,blank=True, on_delete=models.CASCADE, verbose_name='Пособие',
                             related_name='good_urls')
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Проект',
                                related_name='project_urls')

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        verbose_name = 'Ссылка на ютуб'
        verbose_name_plural = 'Ссылки на ютуб'
