# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('article/<slug:slug>/', views.article, name='article'),
]
