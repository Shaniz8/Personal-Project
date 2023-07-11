from django.urls import path

from . import views

# This will instruct the application to render the index view
app_name = "Accounts"
urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('settings/', views.settings, name='settings'),

]