from tkinter import Widget
from django import forms
from django.forms import ModelForm
#from Games.models import Games
from home.game import Game

# class GameForm(ModelForm):
#     class Meta:
#         model = Games
# from Games.models import Games
from home.game import Game 

class GameForm(forms.Form):
    title = forms.CharField(max_length=100)
    dev = forms.CharField(max_length=100)
    publisher = forms.CharField(max_length=100)
    genre = forms.CharField(max_length=100)
    price = forms.FloatField()
