'''Данный модуль используется для рендера страниц проекта, а также для обработки запросов и ответов, 
также с помощью костылей сюда можно засунуть бизнес-логику.'''

from django.shortcuts import render


def index(request):
    '''Рендер Главной страницы'''
    return render(request, 'index.html')


def service(request):
    '''Рендер вкладки "Сервис"'''
    return render(request, 'service.html')


def documentation(request):
    '''Рендер вкладки "Документация"'''
    return render(request, 'documentation.html')


def contacts(request):
    '''Рендер вкладки "Контакты"'''
    return render(request, 'contacts.html')