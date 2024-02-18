from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        'page_title': 'Домашняя страница',
        'welcome_message': 'Добро пожаловать на наш сайт!'
    }
    return render(request, 'home.html', context)


@login_required
def defended(request):
    context = {
        'page_title': 'Страница защищена',
        'welcome_message': 'Эта страница доступна только зарегистрированным пользователям'
    }
    return render(request, 'home.html', context)