from django.urls import path 
from . import views

#URLConf (url configuration)
urlpatterns = [
    path('', views.home, name="home"), #always end routes w/ forward slash
    #path('homepage/', views.search_bar)
]
