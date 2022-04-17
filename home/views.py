from django.shortcuts import render
from django.http import HttpResponse

from Games.models import Games

# Create your views here.
# request handler
def search_games(request):
    if request.method == "POST":
        searched = request.POST['searched']
        games = Games.objects.filter(title__contains=searched)
        return render(request, 'home/search_games.html', {'searched':searched, 'games':games})
    else: 
        return render(request, 'home/search_games.html', {})

def home(request):
    return render(request, 'home/home.html', {'name': 'CS Girlie'})

def search_bar(request):
    #if request.method == "POST":
    return render(request, 'home/search_bar.html', {})

   # else:
        #return render(request, 'home/search_bar.html', {})
