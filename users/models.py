from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import Model
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    telegram = models.CharField(unique=True, max_length=255, null=True, blank=True, verbose_name='Телеграмм')
    instagram = models.CharField(unique=True, max_length=255, null=True, blank=True, verbose_name='Инстаграмм')
    phone = models.CharField(unique=True, null=True, blank=True, max_length=20, verbose_name='Телефон')
    patronymic = models.CharField(max_length=30, blank=True, verbose_name='Отчество')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    email = models.EmailField(unique=True, verbose_name='Почта')
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()


class UserMeta(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=255, verbose_name="Дополнительное поле")
    field_value = models.CharField(max_length=255, verbose_name="Значение")

    class Meta:
        unique_together = ('user', 'field_name')
