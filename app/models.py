from django.db import models
from django.contrib.auth.models import User
import re

# class UserManager(models.Manager):
#     def login_validator(self, post_data):
#         errors = {}
#         if len(post_data["username"]) <= 0:
#             errors["username"] = "username name is required"
        
#         if len(post_data["password"]) <= 0:
#             errors["password"] = "password name is required"

#         # add Bcrypt 
#         return errors
    
#     def register_validator(self, post_data):
#         errors = {}

#         # check for duplicates for username
#         if len(post_data["username"]) <= 0:
#             errors["username"] = "username name is required"
        
#         if len(post_data["password"]) <= 0:
#             errors["password"] = "password name is required"
         
#         # email validation
#         EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#         if not EMAIL_REGEX.match(post_data['email']):    # test whether a field matches the pattern            
#             errors['email'] = "Invalid email address!"
#         return errors
    

# class User():
    # tilte, password, email, first name, last name    
    # Customer : customer linked to this user 
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def get_all_exercises(self):
        pass
    def get_all_workouts(self):
        pass
    def get_exercise(self, id):
        pass
    def get_workout(self, id):
        pass

class Workout(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(User, related_name="workouts", on_delete = models.CASCADE)
    # exercises - list of all exercises belonging
    
    def get_exercises(self):
        print(type(self.exercises.all()))
        return self.exercises.all()

    def __repr__(self):
        return f"title: {self.title}"

    def __str__(self):
        return f"title: {self.title}"


class Exercise(models.Model):
    title = models.CharField(max_length=50)
    sets = models.IntegerField()
    reps = models.IntegerField()
    time = models.IntegerField()
    link = models.TextField()
    description = models.TextField()
    # TODO need to think about this. if user creates workout should we tie it immediately to a workout?
    # Or create a workout (right after user registration, at id zero hence) in database that will refer to all the exercises
    # And then update exercises to other workouts if user wants to create workouts
    user = models.ForeignKey(User, related_name="exercises", on_delete = models.CASCADE)
    workout = models.ForeignKey(Workout, related_name="exercises", on_delete = models.CASCADE, blank=True, null=True)

    def __repr__(self):
        return f"title: {self.title}"
    
    def __str__(self):
        return f"title: {self.title}"