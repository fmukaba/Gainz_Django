from django.db import models
from django.contrib.auth.models import User
import re
import datetime

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
        return self.user.workouts.get(id=id)

    def get_today_workout(self):
        workouts = []
        today = datetime.datetime.today().weekday()
        all_workouts = self.user.workouts.all()
        for w in all_workouts:
            schedule = w.schedule
            if today == 0 and schedule.monday:
                workouts.append(w)
            elif today == 1 and schedule.tuesday:
                workouts.append(w)
            elif today == 2 and schedule.wednesday:
                workouts.append(w)
            elif today == 3 and schedule.thursday:
                workouts.append(w)
            elif today == 4 and schedule.friday:
                workouts.append(w)
            elif today == 5 and schedule.saturday:
                workouts.append(w)
            elif today == 6 and schedule.sunday:
                workouts.append(w)
        return workouts
    def check_id(self, id):
        pass
    
    def completed_workout(self, id):
        today = datetime.datetime.today().weekday()
        workout = self.user.workouts.get(id=id)
        workout.unschedule_today()
    
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
        day = int(day)
        if day == 0:
           schedule.monday = True
        elif day == 1:
           schedule.tuesday = True
        elif day == 2:
           schedule.wednesday = True
        elif day == 3:
           schedule.thursday = True
        elif day == 4:
           schedule.friday = True
        elif day == 5:
           schedule.saturday = True
        elif day == 6:
           schedule.sunday = True 
        schedule.save()

    def unschedule_today(self):
        schedule = self.schedule
        day = datetime.datetime.today().weekday()
        if day == 0:
           schedule.monday = False
        elif day == 1:
           schedule.tuesday = False
        elif day == 2:
           schedule.wednesday = False
        elif day == 3:
           schedule.thursday = False
        elif day == 4:
           schedule.friday = False
        elif day == 5:
           schedule.saturday = False
        elif day == 6:
           schedule.sunday = False 
        schedule.save()
         
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
        
