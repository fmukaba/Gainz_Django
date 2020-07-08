from django.db import models
from django.contrib.auth.models import User
import re

class UserManager(models.Manager):
    def login_validator(self, post_data):
        errors = {}
        if len(post_data["username"]) <= 0:
            errors["username"] = "username name is required"
        
        if len(post_data["password"]) <= 0:
            errors["password"] = "password name is required"

        # add Bcrypt 
        return errors
    
    def register_validator(self, post_data):
        errors = {}

        # check for duplicates for username
        if len(post_data["username"]) <= 0:
            errors["username"] = "username name is required"
        
        if len(post_data["password"]) <= 0:
            errors["password"] = "password name is required"
         
        # email validation
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        return errors

# class User(models.Model):
#     username = models.CharField(max_length=30)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=30)
#     password = models.CharField(max_length=20)
#     confirm_password = models.CharField(max_length=20)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = UserManager()

class Workout(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, related_name="workouts", on_delete = models.CASCADE)
    # exercises - list of all exercises belonging

    def __repr__(self):
        return f"title: {self.title}"

class Exercise(models.Model):
    title = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    description = models.TextField()
    time = models.IntegerField()
    link = models.TextField()
    # TODO need to think about this. if user creates workout should we tie it immediately to a workout?
    # Or create a workout (right after user registration, at id zero hence) in database that will refer to all the exercises
    # And then update exercises to other workouts if user wants to create workouts

    workout = models.ForeignKey(Workout, related_name="exercises", on_delete = models.CASCADE)  # blank=True, null=True

    def __repr__(self):
        return f"title: {self.title}"