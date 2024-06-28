# chatbot/forms.py

from django import forms

#Création du formulaire pour le chat
class ChatForm(forms.Form):
    user_input = forms.CharField(label='Your Message', max_length=800)
