from django.shortcuts import render
from django.http import HttpResponse

# from .models import Experience

# This message will be shown on the index page of the 'Experience' Application
def index(request):
    return render(request, 'Experience.html')

