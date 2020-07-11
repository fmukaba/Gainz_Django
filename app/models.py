from django.db import models
from django.contrib.auth.models import User
import re

# class auth.models.User():
    # username, password, email, first name, last name  
    # workouts - list of all workouts belonging
    # exercises - list of all exercises belonging  
    # Customer - customer linked to this user 
    
class Customer(models.Model):
    username = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def get_all_exercises(self):
        return self.user.exercises.all()
    def get_all_workouts(self):
        pass
    def get_exercise(self, id):
        return self.user.exercises.get(id=id)
    def get_workout(self, id):
        pass

class Workout(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(User, related_name="workouts", on_delete = models.CASCADE)
    # exercises - list of all exercises belonging
    # days - list of days scheduled
    def get_exercises(self):
        print(type(self.exercises.all()))
        return self.exercises.all()

    def __repr__(self):
        return f"title: {self.title}, description: {self.description}"

    def __str__(self):
        return f"title: {self.title}, description: {self.description}"

    def schedule(self, day):
        # if day == 0:
        pass

class Exercise(models.Model):
    title = models.CharField(max_length=50)
    sets = models.IntegerField()
    reps = models.IntegerField()
    time = models.IntegerField()
    link = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(User, related_name="exercises", on_delete = models.CASCADE)
    workouts = models.ManyToManyField(Workout, related_name="exercises")
    
    def __repr__(self):
        return f"title: {self.title}, sets: {self.sets}, description: {self.description}"
    
    def __str__(self):
        return f"title: {self.title}, sets: {self.sets}, description: {self.description}"
        
#  days a workout is scheduled on       
class Workout_days(models.Model):
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()
    workouts = models.ForeignKey(Workout, related_name="days",on_delete = models.CASCADE)