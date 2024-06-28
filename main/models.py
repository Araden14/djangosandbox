from django.db import models
from django.utils.text import slugify

# Modèle pour les articles
class Article(models.Model):
    # Champ pour l'image miniature, facultatif
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    # Champ pour le nom de l'article
    name = models.CharField(max_length=100, default='Untitled')
    # Champ pour le slug, unique pour chaque article
    slug = models.SlugField(unique=True, max_length=100, default='')
    # Champ pour le résumé de l'article
    abstract = models.CharField(max_length=200, default='No abstract available.')
    # Champ pour le contenu de l'article
    content = models.TextField(default='')
    # Champ pour l'auteur de l'article
    author = models.CharField(max_length=100, default='Anonymous')
    # Champ pour le sujet de l'article
    topic = models.CharField(max_length=100, default='General')
    # Champ pour la date de publication, automatiquement ajouté
    publication_date = models.DateTimeField(auto_now_add=True)
    
    # Méthode pour sauvegarder l'article
    def save(self, *args, **kwargs):
        # Générer un slug basé sur le nom si le slug n'existe pas
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    # Méthode pour afficher le nom de l'article
    def __str__(self):
        return self.name

# Modèle pour les conversations
class Conversation(models.Model):
    # Champ pour l'entrée de l'utilisateur
    user_input = models.TextField()
    # Champ pour la réponse du bot
    bot_response = models.TextField()
    # Champ pour la date de création, automatiquement ajouté
    created_at = models.DateTimeField(auto_now_add=True)

    # Méthode pour afficher la date de la conversation
    def __str__(self):
        return f"Conversation at {self.created_at}"
