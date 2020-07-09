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
    

# class auth.models.User():
    # username, password, email, first name, last name  
    # workouts - list of all workouts belonging
    # exercises - list of all exercises belonging  
    # Customer : customer linked to this user 
    
class Customer(models.Model):
    username = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def get_all_exercises(self):
        return self.user.exercises.all()
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
        return f"title: {self.title}, description: {self.description}"

    def __str__(self):
        return f"title: {self.title}, description: {self.description}"

class Exercise(models.Model):
    title = models.CharField(max_length=50)
    sets = models.IntegerField()
    reps = models.IntegerField()
    time = models.IntegerField()
    link = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(User, related_name="exercises", on_delete = models.CASCADE)
    workout = models.ForeignKey(Workout, related_name="exercises", on_delete = models.CASCADE, blank=True, null=True)

    def __repr__(self):
        return f"title: {self.title}, sets: {self.sets}, description: {self.description}"
    
    def __str__(self):
        return f"title: {self.title}, sets: {self.sets}, description: {self.description}"