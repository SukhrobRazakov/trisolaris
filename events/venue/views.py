'''render'''
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string


data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Анджелина Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]


def content(request):
    data = {
        'title': 'Научные и Культурные мероприятия в Екатеринбурге',
        'posts': data_db,
    }

    return render(request, 'venue/content.html', context=data)


def show_post(request, post_id):
    return HttpResponse(f"Отрображение статьи с id = {post_id}")
    

def cities(request):
    return render(request, 'venue/cities.html', {'title': 'Shaharlar'})


def plan(request):
    return render(request, 'venue/plan.html')


def recommend(request):
    return render(request, 'venue/recommend.html', {'title': 'Вам может быть интересно'})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")