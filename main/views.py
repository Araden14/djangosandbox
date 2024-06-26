from django.shortcuts import render, get_object_or_404  # Import the get_object_or_404 function
from .models import Article
from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils import translation
from .forms import ChatForm
import requests
import cohere

co = cohere.Client(api_key="")


def article_list(request):
    articles = Article.objects.all()  # Replace this with your actual query to fetch articles
    return render(request, 'main/article_list.html', {'articles': articles})

def article(request, slug):  
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'main/article.html', {'article': article})

def chat_view(request):
    form = ChatForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        user_input = form.cleaned_data['user_input']
        chat_response = co.chat(model="command-r-plus", message=user_input)
        # Correctly accessing the chat response text
        context['response'] = chat_response.text  # Adjusted based on the correct attribute
    return render(request, 'main/chat.html', context)