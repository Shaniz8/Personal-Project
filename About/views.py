from django.shortcuts import render
from django.http import HttpResponse

# This message will be shown on the index page of the 'About' Application
def index(request):
    return render(request, 'About.html', {})
#     return HttpResponse("This is the About Index Page")