from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from Games.models import Games
from .game import Game
from .read_csv import game_list

from .forms import GameForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import GameForm

def delete_game(request, game_id):
    for i, o in enumerate(game_list):
        if o.gameid == game_id:
            del game_list[i]
            break
    #game = Games.objects.get(pk=game_id)
    return redirect('all-games')

def home(request):
    return render(request, 'home/home.html', {'name': 'CS Girlie'})

def all_games(request):
    searched = ''
    #games_list = Games.objects.all()
    page = request.GET.get('page', 1)
                
    paginator = Paginator(game_list, 25)
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
        gamesToDisplay = []
        if searched:
            #games = Games.objects.filter(title__contains=searched) or Games.objects.filter(dev__contains=searched) or Games.objects.filter(publisher__contains=searched)
            for i, o in enumerate(game_list):
                if searched.lower() in o.title.lower() or searched.lower() in o.dev.lower() or searched.lower() in o.publisher.lower():
                    gamesToDisplay.append(game_list[i])
            #return render(request, 'home/DisplayGames.html', {'searched':searched, 'games':games})
            return render(request, 'home/DisplayGames.html', {'searched':searched, 'games':gamesToDisplay})

        else:
            return all_games(request)
    else:
        return all_games(request)

def add_games(request):
    submitted = False
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            #form.save()
            newGame = Game(0, form.cleaned_data.get("title"), 0, 1, form.cleaned_data.get("dev"), form.cleaned_data.get("publisher"), '', '', '', '', '', 0, 0, 0, 0, 0, '', form.cleaned_data.get("price"))
            newID = int(game_list[-1].gameid)
            newID = newID + 1
            newGame.set_gameid(newID)
            game_list.append(newGame)
            return HttpResponseRedirect('/addGames?submitted=True')

    else:
        form = GameForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home/addGames.html', {'form': form, 'submitted': submitted})
        
def update_game(request, game_id):
    #game = Games.objects.get(pk=game_id)
    form = GameForm(request.POST or None)
    if form.is_valid():
        #form.owners=1
        #form.save()
        for i, o in enumerate(game_list):
            if o.gameid == game_id:
                o.title = form.cleaned_data.get('title')
                o.dev = form.cleaned_data.get('dev')
                o.publisher = form.cleaned_data.get('publisher')
                o.genre = form.cleaned_data.get('genre')
                o.price = form.cleaned_data.get('price')
                break

        return redirect('all-games')
        
    return render(request, 'home/update_game.html', {'form': form})   
