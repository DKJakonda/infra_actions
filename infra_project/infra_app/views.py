"""Пишим модуль."""
from django.http import HttpResponse


def index(request):
    """Пишем функцию."""
    return HttpResponse('У меня получилось!')


def second_page(request):
    """Пишем функцию."""
    return HttpResponse('А это вторая страница')
