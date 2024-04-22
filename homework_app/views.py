from django.shortcuts import render

# Create your views here.

import logging
from django.shortcuts import render
from django.http import HttpResponse # импорт функции HttpResponse из модуля django.http

logger = logging.getLogger(__name__) # создание объекта логгера


def index(request): # определение представления index
    logger.info('Страница "Главная страница" была посещена') # запись сообщения в лог
    html = """
    <h1>Главная страница</h1>
    <p>Текст главной страницы...</p>
    <p>Фреймворк Django - Урок 1. Введение в Django</p>
    <p>Задание:</p>
    <p>Создайте пару представлений в вашем первом приложении:</p>
    <p> — <главная</p>
    <p> — о себе.</p>

    <p>Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой 
    и данными о вашем первом Django-сайте и о вас.</p>

    <p>Сохраняйте в логи данные о посещении страниц.</p>
    """
    title = "Главная страница"
    return render(request, 'index.html', {'html': html, 'title': title}) # возврат ответа

def about(request):
    # Логирование данных о посещении страницы
    logger.info('Страница "О себе" была посещена')

    html = """
    <h1>Обо мне</h1>
    <p>Информация о себе....</p>
    <p>Меня зовут Теймур - это домашнее задание по Django.</p>
    """
    title = "О себе"
    return render(request, 'about.html', {'html': html, 'title': title})

# Обработчик ошибки 404
def error_404(request, exception):
    #return render(request, '404.html', status=404) или так:
    logger.error(f'Страница не найдена')
    title = 'Страница не найдена'
    return render(request, '404.html', {'title': title}, status=404)

# Запуск сервера: py manage.py runserver