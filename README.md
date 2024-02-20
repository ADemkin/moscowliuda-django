### Django сайт для @moscowliuda

#### Запуск
$ poetry run python manage.py migrate
$ poetry run python manage.py createsuperuser
$ poetry run python add_items_to_db.py
$ poetry run python manage.py runserver

#### Линтеры и форматтеры

$ make fmt lint
