from django.shortcuts import render
from django.http import HttpResponse

# This message will be shown on the index page of the 'Accounts' Application
def index(request):
    return render(request, 'Accounts.html')

def signin(request):
    return render(request, 'Accounts/Signin.html')

def settings(request):
    return render(request, 'Accounts/settings.html')

