from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import copy
import operator
import chart_studio.tools as tls

from Games.models import Games
from .game import Game
from .classes import *
from .read_csv import *

from operator import itemgetter

#visualization
from plotly.offline import plot
from plotly.graph_objs import Bar
from plotly.graph_objs import Pie
import plotly.graph_objects as go

from .forms import GameForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import GameForm

def platform_pie(request):
    for i, p in enumerate(platforms):
        p.percentage = (p.total / len(game_list)) * 100

    platforms_s = sorted(platforms, key=lambda Platform: int(Platform.total), reverse=True)

    name = [o.name for o in platforms_s]
    count = [o.total for o in platforms_s]

    pie_div = plot([Bar(x=name, y=count)], output_type= 'div')

    return render(request, 'home/analytics.html', context={'percentages': platforms_s, 'pie': pie_div})

def dev_pie(request):
    for i, d in enumerate(dev_names):
        d.percentage = (d.total_games / len(game_list)) * 100

    dev_names_s = sorted(dev_names, key=lambda Developer: int(Developer.total_games), reverse=True)
    dev_names_s = dev_names_s[:15]

    name = [o.name for o in dev_names_s]
    count = [o.total_games for o in dev_names_s]

    fig = go.Figure(data=[go.Pie(labels=name, values=count)])
    fig.update_layout(
        width= 800, height= 800,
    )

    plot_div = plot(fig, output_type='div')

    return render(request, 'home/DisplayDevs.html', context={'percentages': dev_names_s, 'pie_dev': plot_div})

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
    game = Games.objects.get(pk=game_id)
    form = GameForm(request.POST or None, instance=game)
    if form.is_valid():
        form.owners=1
        form.save()
        return redirect('all-games')
        
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
    #sorted_playtime = sorted(playtimes, key=operator.attrgetter('avg_playtime'), reverse=True)
    sorted_playtime = sorted(playtimes, key=lambda Playtime: int(Playtime.avg_playtime), reverse=True)

    sorted_playtime = sorted_playtime[:10]
    titles = [o.title for o in sorted_playtime]
    play = [int(o.avg_playtime) for o in sorted_playtime]
    
    plot_div = plot([Bar(x=titles, y=play)], output_type= 'div')

    return render(request, 'home/top_playtime.html', context={'plot_div': plot_div})

def highest_rating(request):
    goodRatings = []

    for i, o in enumerate(game_list):
        goodRatings.append(GoodRatings(o.title, o.pos_rate))

    sorted_goodRating = sorted(goodRatings, key=lambda GoodRatings: int(GoodRatings.pos_rate), reverse=True)
    sorted_goodRating = sorted_goodRating[:10]

    return render(request, 'home/highestRating.html', context ={'goodRatings': sorted_goodRating})


def lowest_rating(request):
    badRatings = []

    for i, o in enumerate(game_list):
        badRatings.append(BadRatings(o.title, o.neg_rate))

    sorted_badRating = sorted(badRatings, key=lambda BadRatings: int(BadRatings.neg_rate), reverse=True)
    sorted_badRating = sorted_badRating[:10]

    return render(request, 'home/lowestRating.html', context ={'badRatings': sorted_badRating})

def average_rating(request):
    avg_rating = []

    for i, o in enumerate(game_list):
        avg_rating.append(AverageRating(o.title, o.pos_rate, o.neg_rate))
    

    test = sorted(avg_rating, key=lambda AverageRating: int(AverageRating.avg), reverse=True)

    sorted_avg = test[:100]

    return render(request, 'home/avgRating.html', context ={'avg_rating': sorted_avg})

def popular_genre(request):
    # size = len(genre_list)
    # firstGenre = genre_list[0]
    # bruh = firstGenre.split(';')
    sorted_genreList = sorted(genre_list, key=lambda Genre: int(Genre.count), reverse=True)
    sorted_genreList = sorted_genreList[:15]
    name = [o.name for o in sorted_genreList]
    count = [int(o.count) for o in sorted_genreList]
    
    fig = go.Figure(data=[go.Pie(labels=name, values=count)])
    fig.update_layout(
        width= 800, height= 800,
    )
    #fig.Title("Top Game Genres")
    plot_div = plot(fig, output_type='div')
    
    #plot([Pie(labels = name, values = count)], width = 2 ,output_type= 'div')
    

    return render(request, 'home/popularGenre.html', context ={ 'genre_bar' :  plot_div})
