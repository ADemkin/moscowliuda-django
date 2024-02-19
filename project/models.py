from django.db import models



class Project(models.Model):
    title = models.CharField(verbose_name='Заголовок',max_length=100)
    sub_title = models.CharField(verbose_name='Подзаголовок',max_length=100)
    main_photo = models.ImageField(verbose_name='Главное Фото', upload_to='project_photos')
    description = models.TextField(verbose_name='Описание',max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    url = models.URLField(verbose_name='Ссылка на проект')
