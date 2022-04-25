from django import forms
from django.forms import ModelForm
from Games.models import Games

class GameForm(ModelForm):
    class Meta:
        model = Games
        fields = ('title', 'dev', 'publisher', 'genre', 'price')