from django.urls import path 
from . import views

#URLConf (url configuration)
urlpatterns = [
    #path('hello/', views.say_hello) #always end routes w/ forward slash
    path('homepage/', views.search_bar)
]
