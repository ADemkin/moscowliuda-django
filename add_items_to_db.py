import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moscowliuda.settings')
import django
django.setup()
from goods.models import Photo, Url, TextBook, Project



photo1 = Photo.objects.create(name='Фото 1', photo='photos/photo1.jpg')
photo2 = Photo.objects.create(name='Фото 2', photo='photos/photo2.jpg')
photo3 = Photo.objects.create(name='Фото 3', photo='photos/photo3.jpg')
photo4 = Photo.objects.create(name='Фото 4', photo='photos/photo4.jpg')


url1 = Url.objects.create(name='Ссылка 1', url='https://www.youtube.com/watch?v=BSlfcu4nDQI')
url2 = Url.objects.create(name='Ссылка 2', url='https://www.youtube.com/watch?v=a7jYN_TToCY')
url3 = Url.objects.create(name='Ссылка 3', url='https://www.youtube.com/watch?v=CP14arpa84M')


textbook1 = TextBook.objects.create(
    title='Учебник 1',
    sub_title='Подзаголовок 1',
    price_rub=500,
    main_photo=photo1,
    description='Описание учебника 1'
)
textbook1.secondary_photos.add(photo2, photo3)
textbook1.urls.add(url1, url2)

textbook2 = TextBook.objects.create(
    title='Учебник 2',
    sub_title='Подзаголовок 2',
    price_rub=600,
    main_photo=photo2,
    description='Описание учебника 2'
)
textbook2.secondary_photos.add(photo1, photo4)
textbook2.urls.add(url2, url3)


project1 = Project.objects.create(
    title='Проект 1',
    sub_title='Подзаголовок 1',
    main_photo=photo3,
    description='Описание проекта 1'
)
project1.secondary_photos.add(photo1, photo2)
project1.urls.add(url1, url3)

project2 = Project.objects.create(
    title='Проект 2',
    sub_title='Подзаголовок 2',
    main_photo=photo4,
    description='Описание проекта 2'
)
project2.secondary_photos.add(photo2, photo3)
project2.urls.add(url2)

print('База данных успешно заполнена!')