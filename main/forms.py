# chatbot/forms.py

from django import forms

class ChatForm(forms.Form):
    user_input = forms.CharField(label='Your Message', max_length=800)
