import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moscowliuda.settings')
import django

django.setup()
from goods.models import Photo, Url, Good, Project


def create_database_test_values():
    try:
        good1 = Good.objects.create(
            title='Good 1',
            sub_title='Sub Title 1',
            price_rub=500,
            main_photo='photos/photo1.jpg',
            description='Description for Good 1'
        )

        good2 = Good.objects.create(
            title='Good 2',
            sub_title='Sub Title 2',
            price_rub=600,
            main_photo='photos/photo2.jpg',
            description='<b>Жырный текст</b><br>Обычный текст<p>Параграф</p>'
        )

        project1 = Project.objects.create(
            title='Project 1',
            sub_title='Sub Title 1',
            main_photo='photos/photo2.jpg',
            description='Description for Project 1'
        )

        project2 = Project.objects.create(
            title='Project 2',
            sub_title='Sub Title 2',
            main_photo='photos/photo1.jpg',
            description='Description for Project 2'
        )

        # photo1 = Photo.objects.create(name='Photo 1', photo='photos/photo1.jpg', good=good1, project=project1)
        photo2 = Photo.objects.create(name='Photo 2', photo='photos/photo2.jpg', good=good1, project=project1)
        photo3 = Photo.objects.create(name='Photo 3', photo='photos/photo3.jpg', good=good2, project=project2)
        photo4 = Photo.objects.create(name='Photo 4', photo='photos/photo4.jpg', good=good2, project=project2)

        url1 = Url.objects.create(name='Url 1', url='https://www.youtube.com/watch?v=1', good=good1, project=project1)
        url2 = Url.objects.create(name='Url 2', url='https://www.youtube.com/watch?v=2', good=good1, project=project1)
        url3 = Url.objects.create(name='Url 3', url='https://www.youtube.com/watch?v=3', good=good2, project=project2)
        url4 = Url.objects.create(name='Url 4', url='https://www.youtube.com/watch?v=4', good=good2, project=project2)

        print('Testing set in DB created successfully')
    except Exception as e:
        print(f'[ERROR] Cannot to create test dataset in db: {e}')
        return


if __name__ == '__main__':
    create_database_test_values()
