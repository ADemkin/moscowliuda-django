# Generated by Django 5.0.2 on 2024-02-20 13:40

import django.db.models.deletion
import goods.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('name', models.CharField(max_length=100, verbose_name='Название фото')),
                ('photo', models.ImageField(upload_to='photos/', verbose_name='Фото'))
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Ссылка на ютуб',
                'verbose_name_plural': 'Ссылки на ютуб',
            },
        ),
        migrations.CreateModel(
            name='TextBook',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('sub_title', models.CharField(max_length=100, verbose_name='Подзаголовок')),
                ('price_rub', models.IntegerField(verbose_name='Цена')),
                ('description', models.TextField(max_length=4000, verbose_name='Описание')),
                (
                    'created_at',
                    models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
                ),
                (
                    'main_photo',
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='main_photo_of',
                        to='goods.photo',
                        verbose_name='Главное фото',
                    ),
                ),
                (
                    'secondary_photos',
                    models.ManyToManyField(
                        blank=True,
                        related_name='text_books',
                        to='goods.photo',
                        verbose_name='Второстепенные фото',
                    ),
                ),
                (
                    'urls',
                    models.ManyToManyField(
                        blank=True,
                        related_name='text_books',
                        to='goods.url',
                        verbose_name='Ссылки на ютуб',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Учебник',
                'verbose_name_plural': 'Учебники',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('sub_title', models.CharField(max_length=100, verbose_name='Подзаголовок')),
                ('description', models.TextField(max_length=4000, verbose_name='Описание')),
                (
                    'created_at',
                    models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
                ),
                (
                    'main_photo',
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='main_photo_of_project',
                        to='goods.photo',
                        verbose_name='Главное фото',
                    ),
                ),
                (
                    'secondary_photos',
                    models.ManyToManyField(
                        blank=True,
                        related_name='projects',
                        to='goods.photo',
                        verbose_name='Второстепенные фото',
                    ),
                ),
                (
                    'urls',
                    models.ManyToManyField(
                        blank=True,
                        related_name='projects',
                        to='goods.url',
                        verbose_name='Ссылки на ютуб',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]
