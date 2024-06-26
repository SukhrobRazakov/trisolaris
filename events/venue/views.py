"""render"""
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView

from .models import Venue

#
# from .forms import AddPostForm, UploadFileForm
# from .models import Venue, Category, TagPost, UploadFiles

from .utils import DataMixin

class VenueHome(DataMixin, ListView):
    template_name = 'venue/index.html'
    context_object_name = 'posts'
    title_page = 'Главная страница'
    cat_selected = 0

    def get_queryset(self):
        return Venue.published.all().select_related('cat')


@login_required
def about(request):
    contact_list = Venue.published.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'venue/about.html',
                  {'title': 'О сайте', 'page_obj': page_obj})


class ShowPost(DataMixin, DetailView):
    template_name = 'venue/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Venue.published, slug=self.kwargs[self.slug_url_kwarg])


class AddPage(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    # form_class = AddPostForm
    template_name = 'venue/addpage.html'
    title_page = 'Добавление статьи'
    permission_required = 'venue.add_venue' # <приложение>.<действие>_<таблица>

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


# class UpdatePage(PermissionRequiredMixin, DataMixin, UpdateView):
#     # model = Venue
#     fields = ['title', 'content', 'photo', 'is_published', 'cat']
#     template_name = 'venue/addpage.html'
#     success_url = reverse_lazy('home')
#     title_page = 'Редактирование статьи'
#     permission_required = 'venue.change_venue'


@permission_required(perm='venue.add_venue', raise_exception=True)
def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


class VenueCategory(DataMixin, ListView):
    template_name = 'venue/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Venue.published.filter(cat__slug=self.kwargs['cat_slug']).select_related("cat")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(context,
                                      title='Категория - ' + cat.name,
                                      cat_selected=cat.pk,
                                      )


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


class TagPostList(DataMixin, ListView):
    template_name = 'venue/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        # return self.get_mixin_context(context, title='Тег: ' + tag.tag)

    def get_queryset(self):
        return Venue.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')


data_db = [
    {
        "id": 1,
        "title": "Анджелина Джоли",
        "content": "Анджелина Джоли",
        "is_published": True,
    },
    {
        "id": 2,
        "title": "Марго Робби",
        "content": "Биография Марго Робби",
        "is_published": False,
    },
    {
        "id": 3,
        "title": "Джулия Робертс",
        "content": "Биография Джулия Робертс",
        "is_published": True,
    },
]


def content(request):
    data = {
        "title": "Научные и Культурные мероприятия в Екатеринбурге",
        "posts": data_db,
    }

    return render(request, "venue/content.html", context=data)


def show_post(request, post_id):
    return HttpResponse(f"Отрображение статьи с id = {post_id}")


def cities(request):
    return render(request, "venue/cities.html", {"title": "Мероприятия города"})

def kurgan(request):
    return render(request, "venue/kurgan.html", {"title": "Научные и Культурные мероприятия в Кургане"})


def plan(request):
    return render(request, "venue/plan.html", {"title": "Избранное"})


def recommend(request):
    return render(
        request, "venue/recommend.html", {"title": "Вам может быть интересно"}
    )


# def page_not_found(request, exception):
#     return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def chernovik(request):
    return render(request, "venue/chernovik.html", {"title": "chernovik"})


def regis(request):
    return render(request, "venue/regis.html", {"title": "Личный кабинет организатора"})


def sub(request):
    return render(request, "venue/sub.html", {"title": "Войти"})


def cobinet(request):
    return render(request, "venue/cobinet.html")


def ch(request):
    return render(request, "venue/ch.html")


def redactor(request):
    return render(request, "venue/redactor.html")

def public(request):
    return render(request, "venue/public.html", {"title": "Статистика мероприятие"})


def obr(request):
    return render(request, "venue/obr.html", {"title": "Екатеринбург Обучение и образование"})

def sea(request):
    return render(request, "venue/sea.html", {"title": "Найти мероприятия в Екатеринбурге"})

def opisaniya(request):
    return render(request, "venue/opisaniya.html", {"title": "ITISconf–2024 20 июня 2024"})

def chat(request):
    return render(request, 'venue/chat.html')