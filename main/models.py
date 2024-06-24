from django.db import models
from django.utils.text import slugify

class Article(models.Model):
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    name = models.CharField(max_length=100, default='Untitled')
    slug = models.SlugField(unique=True, max_length=100, default='')
    abstract = models.CharField(max_length=200, default='No abstract available.')
    content = models.TextField(default='')
    author = models.CharField(max_length=100, default='Anonymous')
    topic = models.CharField(max_length=100, default='General')
    publication_date = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
