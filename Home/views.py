from django.shortcuts import render
from django.http import HttpResponse

# This message will be shown on the index page of the 'Home' Application
def index(request):
    return render(request, 'Home.html', {})

