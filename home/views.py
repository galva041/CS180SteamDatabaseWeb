from django.shortcuts import render
from django.http import HttpResponse

from Games.models import Games

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
# request handler
def search_games(request):
    if request.method == "POST":
        searched = request.POST['searched']
        if searched:
            games = Games.objects.filter(title__contains=searched) or Games.objects.filter(dev__contains=searched) or Games.objects.filter(publisher__contains=searched)
            return render(request, 'home/search_games.html', {'searched':searched, 'games':games})
            #return render(request, 'home/allGames.html', {'searched':searched, 'games':games})
        else:
            return allGames(request)
    else: 
        return render(request, 'home/search_games.html', {})

def home(request):
    return render(request, 'home/home.html', {'name': 'CS Girlie'})

#def search_bar(request):
    #if request.method == "POST":
    #return render(request, 'home/search_bar.html', {})
   # else:
        #return render(request, 'home/search_bar.html', {})

def allGames(request):
    games_list = Games.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(games_list, 25)
    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        games = paginator.page(1)
    except EmptyPage:
        games = paginator.page(paginator.num_pages)

    return render(request, 'home/allGames.html', {'games': games})
    
