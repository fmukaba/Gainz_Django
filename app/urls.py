from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('login', views.login),
    path('register', views.register),
    path('home', views.home),
    path('logout', views.logout),
    path('list_exercises', views.list_exercises),
    path('add', views.add),
    path('add/create_exercise', views.create_exercise),
    path('help', views.help)
]
