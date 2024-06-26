# main/urls.py

from django.urls import path
from . import views

urlpatterns = [

    path('', views.article_list, name='article_list'),
    path('article/<slug:slug>/', views.article, name='article'),
    path('chat/', views.chat_view, name='chat_view'),


]
