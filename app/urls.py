from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('login', views.login),
    path('register', views.register),
    path('home', views.home),
    path('logout', views.logout),
    path('list_exercises', views.list_exercises),
    path('list_workouts', views.list_workouts),
    path('schedule', views.schedule),
    path('home/schedule', views.schedule),
    path('add', views.add),
    path('add/create_exercise', views.create_exercise),
    path('add/create_workout', views.create_workout),
    path('help', views.help)
]
