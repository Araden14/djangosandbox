# main/admin.py

from django.contrib import admin
from .models import Article
# Enregistrer le modèle Article dans l'interface d'administration
admin.site.register(Article)
