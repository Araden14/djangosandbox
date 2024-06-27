# views.py

from django.shortcuts import render, get_object_or_404  # Import the get_object_or_404 function
from .models import Article
from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils import translation
from .forms import ChatForm
import cohere
import logging 


COHERE_API_KEY = ""
co = cohere.Client(COHERE_API_KEY)
logging.basicConfig(level=logging.INFO)


def article_list(request):
    articles = Article.objects.all()  # Replace this with your actual query to fetch articles
    return render(request, 'main/article_list.html', {'articles': articles})

def article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'main/article.html', {'article': article})

def chat_view(request):
    form = ChatForm(request.POST or None)
    context = {'form': form, 'chat_history': request.session.get('chat_history', [])}

    if form.is_valid():
        user_input = form.cleaned_data['user_input']
        try:
            # Construct the prompt from the chat history
            prompt = ""
            for entry in context['chat_history']:
                prompt += f"<br>User: {entry['user_input']}<br>Bot: {entry['chat_response']}"
            prompt += f"""You are a funny AI assistant. Format the following response using simple HTML tags to enhance readability without breaking the structure of the web page. 
                Use <b> for bold, <i> for italics, <br> for line breaks, and <p> for paragraphs. Do not use any other HTML tags or attributes. Don't mention the text is HTML formatted. Ensure the HTML is well-formed Prompt:<br>User: {user_input}<br>Bot:"""

            print(f'LE PROMPT ICI : {prompt} =======================================')

            chat_response = co.generate(
                model="command-r-plus",
                prompt=prompt,
                max_tokens=8000,
            )
            response_text = chat_response.generations[0].text.strip()
            print(response_text)

            # Update the conversation history
            chat_entry = {'user_input': user_input, 'chat_response': response_text}
            context['chat_history'].append(chat_entry)
            
            # Save the updated conversation history in the session
            request.session['chat_history'] = context['chat_history']
        except Exception as e:
            logging.error(f"Error generating chat response: {e}")
            context['error'] = "Failed to generate chat response. Please try again later."
    else:
        logging.info("Form is not valid")

    return render(request, 'main/chat.html', context)
