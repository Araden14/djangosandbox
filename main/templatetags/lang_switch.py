from django import template
from django.urls import translate_url

register = template.Library()

@register.simple_tag(takes_context=True)
def switch_lang(context, lang):
    request = context['request']
    return translate_url(request.path, lang)