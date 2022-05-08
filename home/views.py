from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import copy
import operator

from Games.models import Games
from .game import Game
from .playtime import Playtime
from .read_csv import game_list
from .ratings import GoodRatings
from .ratings import BadRatings


#visualization
from plotly.offline import plot
from plotly.graph_objs import Bar

from .forms import GameForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import GameForm

def delete_game(request, game_id):
    for i, o in enumerate(game_list):
        if int(o.gameid) == int(game_id):
            del game_list[i]
            break
    return redirect('all-games')

def home(request):
    return render(request, 'home/home.html', {'name': 'CS Girlie'})

def all_games(request):
    searched = ''
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
            for i, o in enumerate(game_list):
                if searched.lower() in o.title.lower() or searched.lower() in o.dev.lower() or searched.lower() in o.publisher.lower():
                    gamesToDisplay.append(game_list[i])
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
    form = GameForm(request.POST or None)
    if form.is_valid():
        for i, o in enumerate(game_list):
            if int(o.gameid) == int(game_id):
                o.title = form.cleaned_data.get('title')
                o.dev = form.cleaned_data.get('dev')
                o.publisher = form.cleaned_data.get('publisher')
                o.genre = form.cleaned_data.get('genre')
                o.price = form.cleaned_data.get('price')
                break
        return redirect('all-games')        
    return render(request, 'home/update_game.html', {'form': form})

def most_playtime(request) :

    #playtimes = [o.avg_playtime for o in game_list]
    #titles = [o.title for o in game_list]

    playtimes = []

    for i, o in enumerate(game_list):
        playtimes.append(Playtime(o.title, o.avg_playtime))

    #playtimes.sort(reverse=True)
    #titles.sort(reverse=True)
    
    

    #playtime = [Playtime(titles, playtimes)]
    #playtime.sort(key=lambda x: x.count, reverse=True)
    sorted_playtime = sorted(playtimes, key=operator.attrgetter('avg_playtime'), reverse=True)
    sorted_playtime = sorted_playtime[:10]
    # for title, avg_playtime in enumerate(sorted_playtime):
    #     plot_div = plot([Bar(x=title, y=avg_playtime)], output_type= 'div')

    

    return render(request, 'home/analytics.html', context={'playtimes': sorted_playtime})

def highest_rating(request):
    goodRatings = []

    for i, o in enumerate(game_list):
        goodRatings.append(GoodRatings(o.title, o.pos_rate))


    sorted_goodRating = sorted(goodRatings, key = operator.attrgetter('pos_rate'), reverse=True)
    sorted_goodRating = sorted_goodRating[:10]

    return render(request, 'home/highestRating.html', context ={'goodRatings': sorted_goodRating})


def lowest_rating(request):
    badRatings = []

    for i, o in enumerate(game_list):
        badRatings.append(BadRatings(o.title, o.neg_rate))


    sorted_badRating = sorted(badRatings, key = operator.attrgetter('neg_rate'), reverse=True)
    sorted_badRating = sorted_badRating[:10]

    return render(request, 'home/lowestRating.html', context ={'badRatings': sorted_badRating})
