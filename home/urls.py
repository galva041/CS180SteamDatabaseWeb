from django.urls import path 
from . import views

#URLConf (url configuration)
urlpatterns = [
    path('', views.home, name="home"), #always end routes w/ forward slash
    #path('search', views.search_bar, name="search-bar"),
    path('searchGames/', views.search_games, name="search-games"),
    path('allGames/', views.all_games, name="all-games" ),
    path('addGames/', views.add_games, name="add-games"),
    path('delete_game/<game_id>', views.delete_game, name='delete_game'),
    path('update_game/<game_id>', views.update_game, name='update-game'),
    path('most_playtime/', views.most_playtime, name='most-playtime'),
]
