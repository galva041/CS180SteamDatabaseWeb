from django.urls import path 
from . import views

#URLConf (url configuration)
urlpatterns = [
    path('', views.home, name="home"), #always end routes w/ forward slash
    path('search', views.search_bar, name="search-bar"),
    path('search_games/', views.search_games, name="search-games")
]
