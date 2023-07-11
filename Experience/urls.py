
from django.urls import path

from . import views

# This will instruct the application to render the index view
app_name = "Experience"
urlpatterns = [
    path('', views.index, name='index'),
]