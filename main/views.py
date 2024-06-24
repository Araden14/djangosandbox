from django.shortcuts import render, get_object_or_404  # Import the get_object_or_404 function
from .models import Article


def article_list(request):
    articles = Article.objects.all()  # Replace this with your actual query to fetch articles
    return render(request, 'main/article_list.html', {'articles': articles})

def article(request, slug):  
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'main/article.html', {'article': article})

def base(request):
    return render(request, 'main/base.html')