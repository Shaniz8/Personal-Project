from django.shortcuts import render
from django.http import HttpResponse

# This message will be shown on the index page of the 'Experience' Application
def index(request):
    return HttpResponse("Hello, this is the Experience index page.")

