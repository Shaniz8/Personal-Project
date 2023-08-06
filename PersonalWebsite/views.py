from django.shortcuts import render
from django.http import HttpResponse

def base(request):
    return render(request, 'Home.html', {}),

# def about(request):
#     return render(request, 'About.html', {}),
#
# def accounts(request):
#     return render(request, 'Accounts.html', {}),
#
# def experience(request):
#     return render(request, 'Experience.html', {}),

