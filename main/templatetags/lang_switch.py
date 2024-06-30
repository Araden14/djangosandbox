from django import template
from django.urls import translate_url

# Créer un tag pour changer la langue
register = template.Library()
# Prendre le contexte et la langue
@register.simple_tag(takes_context=True)
def switch_lang(context, lang):
    request = context['request']
    return translate_url(request.path, lang)