from django.contrib.auth.models import AbstractUser
from django.db.models import Model
from django.db import models
from django.utils.translation import gettext_lazy as _


class MoscowUser(AbstractUser):
    telegram = models.CharField(unique=True, max_length=255, null=True, blank=True, verbose_name='Телеграмм')
    instagram = models.CharField(unique=True, max_length=255, null=True, blank=True, verbose_name='Инстаграмм')
    phone = models.CharField(unique=True, max_length=20, verbose_name='Телефон')

    firstname = models.CharField(max_length=30, blank=True, verbose_name='Имя')
    surname = models.CharField(max_length=30, blank=True, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=30, blank=True, verbose_name='Отчество')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    email = models.EmailField(_("email address"),
                              unique=True,
                              error_messages={
                                  "unique": _("A user with that email already exists."),
                              })
    first_name = None
    last_name = None

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)



class UserMeta(Model):
    user = models.ForeignKey(MoscowUser, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=255, verbose_name="Дополнительное поле")
    field_value = models.CharField(max_length=255, verbose_name="Значение")

    class Meta:
        unique_together = ('user', 'field_name')
