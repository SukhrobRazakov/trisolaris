"""
URL configuration for events project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, register_converter
from venue import views


urlpatterns = [
    path("", views.content, name="content"),  # sayt ka malumot ciqariw http://127.0.0.1:8000
    path("post/<int:post_id>/", views.show_post, name="post"),  # content
    path("cities/", views.cities, name="cities"),  # waharlar
    path("plan/", views.plan, name="plan"),  # izbrinnie
    path("recommend/", views.recommend, name="recommend"),  # мой выбор    chernovik
    path("chernovik/", views.chernovik, name="chernovik"),
    path("regis/", views.regis, name="regis"),
    path("sub/", views.sub, name="sub"),
    path("cobinet/", views.cobinet, name="cobinet"),
    path("ch/", views.ch, name="ch"),
    path("redactor/", views.redactor, name="redactor"),
    path("kurgan/", views.kurgan, name="kurgan"),
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('public/', views.public, name='public'),
    path('obr/', views.obr, name='obr'),
    path('sea/', views.sea, name='sea'),
    path('opisaniya/', views.opisaniya, name='opisaniya'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),    
    # path('category/<slug:cat_slug>/', views.VenueCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.TagPostList.as_view(), name='tag'),
    # path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),
    path('chat/', views.chat, name='chat'),
]
