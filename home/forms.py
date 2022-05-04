from tkinter import Widget
from django import forms
from django.forms import ModelForm
# from Games.models import Games
from home.game import Game 

# class GameForm(ModelForm):
#     class Meta:
#         model = Game
#         fields = ('title', 'dev', 'publisher', 'genre', 'price')

class GameForm(forms.Form):
    title = forms.CharField(max_length=100)
    dev = forms.CharField(max_length=100)
    publisher = forms.CharField(max_length=100)
    genre = forms.CharField(max_length=100)
    price = forms.FloatField()

    # def __init__ (self, title, dev, publisher, genre, price):
    #     self.title = title
    #     self.dev = dev
    #     self.publisher = publisher
    #     self.genre = genre
    #     self.price = price