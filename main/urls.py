from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the homepage or main list view of articles
    path('', views.article_list, name='article_list'),

    # URL pattern for viewing individual articles by slug
    # This pattern captures a slug from the URL and passes it to the article view
    path('article/<slug:slug>/', views.article, name='article'),

    # URL pattern for the chat feature
    path('chat/', views.chat_view, name='chat_view'),
]
