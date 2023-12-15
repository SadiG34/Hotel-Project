from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

from .models import *
menu = [
    {'title': 'О сайте', 'url_name': 'about'}, 
    {'title': 'Добавить статью', 'url_name': 'add_page'}, 
    {'title': 'Обратная связь', 'url_name': 'contact'}, 
    {'title': "Войти", 'url_name': 'login'}, 
        ]

def index(reguest):
    posts = Women.objects.all()
    context = {
    'posts': posts, 
    'menu': menu, 
    'title': 'Главная страница'
    }
    return render(reguest, 'women/index.html', context=context)


def about(reguest):
    return render(reguest, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

def addpage(reguest):
    return HttpResponse(f'Добавление статьи')

def contact(reguest):
    return HttpResponse(f'Обратная связь')

def login(reguest):
    return HttpResponseNotFound('Авторизация')

def pageNotFound(reguest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(reguest, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')