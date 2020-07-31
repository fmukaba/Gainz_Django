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
    path('add_workout', views.add_workout),
    path('add_exercise', views.add_exercise),
    path('completed/<int:id>', views.completed_workout),
    path('view_workout/<int:id>', views.view_workout), 
    path('view_exercise/<int:id>', views.view_exercise),
    path('delete_workout/<int:id>', views.delete_workout), 
    path('delete_exercise/<int:id>', views.delete_exercise),
    path('edit_workout/<int:id>', views.edit_workout), 
    path('edit_exercise/<int:id>', views.edit_exercise)
]
