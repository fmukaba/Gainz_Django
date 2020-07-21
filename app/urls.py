from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('login', views.login),
    path('logout', views.logout),
    path('register', views.register),
    path('help', views.help),
    path('home', views.home),
    path('list_workouts', views.list_workouts),
    path('list_exercises', views.list_exercises),
    path('add/create_workout', views.create_workout),
    path('add/create_exercise', views.create_exercise),
    path('completed/<int:id>', views.completed_workout),
    path('view/<int:id>', views.view_workout),    
]
