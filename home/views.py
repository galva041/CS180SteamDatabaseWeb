from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request handler

def say_hello(request):
    return render(request, 'hello.html', {'name' : 'CS Girlies'})

def search_bar(request):
    return render(request, 'homepage.html')