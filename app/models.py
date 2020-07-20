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
        return self.user.workouts.all()
    def get_exercise(self, id):
        return self.user.exercises.get(id=id)
    def get_workout(self, id):
        pass
    def get_today_workout(self):
        pass

#  days a workout is scheduled on       
class Schedule(models.Model):
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()
    # workout - workout linked to this schedule

    def __repr__(self):
        return f"monday: {self.monday}, tuesday: {self.tuesday}, friday: {self.friday}"
    
    def __str__(self):
        return f"monday: {self.monday}, tuesday: {self.tuesday}, friday: {self.friday}"

class Workout(models.Model):
    
    title = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(User, related_name="workouts", on_delete = models.CASCADE)
    schedule = models.OneToOneField(Schedule, related_name="workout" ,on_delete = models.CASCADE)
    # exercises - list of all exercises belonging
    # days - list of days scheduled
    def get_exercises(self):
        return self.exercises.all()

    def __repr__(self):
        return f"title: {self.title}, description: {self.description}"

    def __str__(self):
        return f"title: {self.title}, description: {self.description}"

    def create_schedule(self): 
        return Schedule(monday=False, tuesday=False, 
                        wednesday=False, thursday=False,
                        friday=False, saturday=False, sunday=False)
                        
    def set_schedule(self, day):
        schedule = self.schedule
        if day == 1:
           schedule.monday = True
        elif day == 2:
           schedule.tuesday = True
        elif day == 3:
           schedule.wednesday = True
        elif day == 4:
           schedule.thursday = True
        elif day == 5:
           schedule.friday = True
        elif day == 6:
           schedule.saturday = True
        elif day == 7:
           schedule.sunday = True 
        self.schedule = schedule
        self.save()
        print(self.schedule)
         

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
        
