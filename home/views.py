from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import copy
import operator

from Games.models import Games
from .game import Game
from .playtime import Playtime
from .read_csv import game_list

#visualization
from plotly.offline import plot
from plotly.graph_objs import Bar

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
            #form.save()
           #new_game = Game(0, form.title, )
            return HttpResponseRedirect('/addGames?submitted=True')

    else:
        form = GameForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home/addGames.html', {'form': form, 'submitted': submitted})
        
def update_game(request, game_id):
    game = Games.objects.get(pk=game_id)
    form = GameForm(request.POST or None, instance=game)
    if form.is_valid():
        form.owners=1
        form.save()
        return redirect('all-games')
        
    return render(request, 'home/update_game.html', {'form': form, 'game': game})   

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