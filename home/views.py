from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from Games.models import Games
#from .game import Game
#from .read_csv import game_list

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import GameForm

def delete_game(request, game_id):
    game = Games.objects.get(pk=game_id)
    game.delete()
    return redirect('all-games')

def home(request):
    return render(request, 'home/home.html', {'name': 'CS Girlie'})

def all_games(request):
    searched = ''
    games_list = Games.objects.all()
    page = request.GET.get('page', 1)
                
    paginator = Paginator(games_list, 25)
    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        games = paginator.page(1)
    except EmptyPage:
        games = paginator.page(paginator.num_pages)

    return render(request, 'home/DisplayGames.html', {'':searched,'games': games})

def search_games(request):
    if request.method == "POST":
        searched = request.POST['searched']
        if searched:
            games = Games.objects.filter(title__contains=searched) or Games.objects.filter(dev__contains=searched) or Games.objects.filter(publisher__contains=searched)
            return render(request, 'home/DisplayGames.html', {'searched':searched, 'games':games})
        else:
            return all_games(request)
    else:
        return all_games(request)

def add_games(request):
    submitted = False
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addGames?submitted=True')

    else:
        form = GameForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home/addGames.html', {'form': form, 'submitted': submitted})
        
   
