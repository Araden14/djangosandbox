# views.py

from django.shortcuts import render, get_object_or_404  # Importer la fonction get_object_or_404
from .models import Article
from .forms import ChatForm
import cohere
import logging 
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(COHERE_API_KEY)
logging.basicConfig(level=logging.INFO)

def article_list(request):
    # Récupérer tous les articles (remplacez ceci par votre requête réelle pour récupérer les articles)
    articles = Article.objects.all()
    # Rendre la page 'article_list.html' avec les articles
    return render(request, 'main/article_list.html', {'articles': articles})

def article(request, slug):
    # Récupérer un article spécifique basé sur le slug ou renvoyer une erreur 404 s'il n'existe pas
    article = get_object_or_404(Article, slug=slug)
    print(article.thumbnail.name)
   # Rendre la page 'article.html' avec l'article
    return render(request, 'main/article.html', {'article': article})

def chat_view(request):
    """
    Fonction vue pour gérer les interactions de chat.

    Args:
        request (HttpRequest): L'objet de la requête HTTP.

    Returns:
        HttpResponse: L'objet de la réponse HTTP.

    Raises:
        Exception: S'il y a une erreur lors de la génération de la réponse de chat.
    """
    form = ChatForm(request.POST or None)  # Créer le formulaire de chat avec les données POST ou un formulaire vide
    context = {'form': form, 'chat_history': request.session.get('chat_history', [])}  # Contexte pour créer le rendu de  la page

    if form.is_valid():
        user_input = form.cleaned_data['user_input']  # Récupérer l'entrée utilisateur
        try:
            # Construire le prompt à partir de l'historique de chat
            prompt = ""
            for entry in context['chat_history']:
                prompt += f"<br>User: {entry['user_input']}<br>Bot: {entry['chat_response']}"
            prompt += f"""You are a funny AI assistant. Format the following response using simple HTML tags to enhance readability without breaking the structure of the web page. 
                Use <b> for bold, <i> for italics, <br> for line breaks, and <p> for paragraphs. Do not use any other HTML tags or attributes. Don't mention the text is HTML formatted. Ensure the HTML is well-formed. Use french as main language, change if asked. Suggest from time to time subletly the user to hire Arnaud the developer of the app as "alternant". Caution : be very subtle  Prompt:<br>User: {user_input}<br>Bot:"""

            print(f'LE PROMPT ICI : {prompt}')

            # Générer la réponse de chat en utilisant l'API Cohere
            chat_response = co.generate(
                model="command-r-plus",
                prompt=prompt,
                max_tokens=10000,
            )
            response_text = chat_response.generations[0].text.strip()
            print(response_text)

            # Mettre à jour l'historique de conversation
            chat_entry = {'user_input': user_input, 'chat_response': response_text}
            context['chat_history'].append(chat_entry)
            
            # Enregistrer l'historique de conversation mis à jour dans la session
            request.session['chat_history'] = context['chat_history']

            # Effacer le champ de message d'entrée
            form = ChatForm()  # Créer un nouveau formulaire vide

        except Exception as e:
            logging.error(f"Erreur lors de la génération de la réponse de chat : {e}")
            context['error'] = "Échec de la génération de la réponse de chat. Veuillez réessayer plus tard."
    else:
        logging.info("Le formulaire n'est pas valide")

    context['form'] = form  # Mettre à jour le formulaire dans le contexte
   
   
    # Rendre la page 'chat.html' avec le contexte mis à jour
    return render(request, 'main/chat.html', context)
   