from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def home(request):
    if request.user.is_authenticated:
        user = request.user
        context = {
            'page_title': 'Домашняя страница',
            'welcome_message': f'Добро пожаловать на наш сайт! Зарегистрированный пользователь {user.email}'
    }
    else:
        context = {
            'page_title': 'Домашняя страница',
            'welcome_message': 'Добро пожаловать на наш сайт! Не зарегистрированный пользователь'
        }
    return render(request, 'home.html', context)


@login_required
def defended(request):
    context = {
        'page_title': 'Страница защищена',
        'welcome_message': 'Эта страница доступна только зарегистрированным пользователям'
    }
    return render(request, 'home.html', context)