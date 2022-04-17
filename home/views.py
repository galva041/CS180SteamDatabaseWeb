from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request handler

def home(request):
    return render(request, 'home/home.html', {'name': 'CS Girlie'})

def search_bar(request):
    #if request.method == "POST":
    return render(request, 'home/search_bar.html', {})

   # else:
        #return render(request, 'home/search_bar.html', {})
