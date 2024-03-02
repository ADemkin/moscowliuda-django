from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from goods.models import Good, Project


class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Главная страница'
        if self.request.user.is_authenticated:
            context['welcome_message'] = (f'Добро пожаловать на главную страницу,'
                                          f' зарегистрированный пользователь {self.request.user.email}!')
        else:
            context['welcome_message'] = 'Добро пожаловать на главную страницу, гость!'

        goods = Good.objects.all().prefetch_related('good_photos', 'good_urls')
        projects = Project.objects.all().prefetch_related('project_photos', 'project_urls')
        context['good_list'] = render_to_string(template_name='good_list.html', context={'goods': goods})
        context['project_list'] = render_to_string('project_list.html', {'projects': projects})
        return context


@login_required
def defended(request):
    context = {
        'page_title': 'Страница защищена',
        'welcome_message': 'Эта страница доступна только зарегистрированным пользователям'
    }
    return render(request, 'home.html', context)
