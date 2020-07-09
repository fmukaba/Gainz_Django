from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, CreateExerciseForm
from .models import Workout, Exercise, Customer

def login(request):
    if request.method == "GET":
        form = LoginForm()
        context = { "logForm": form }

        return render(request, "login.html", context)
    else:   
        next = request.POST['next']
        form = LoginForm(request.POST)
        errors = form.errors
        print(errors)
        if not form.is_valid():
            for key, value in errors.items():
                # the message object will be held until the next time a page is rendered
                messages.error(request, value)
            return redirect("/login")
        else: 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            if next:
                return redirect(next)
            return redirect("/home")

def register(request):
    if request.method == "GET":
        form = RegisterForm()
        context = { "regForm": form }
        return render(request, "register.html", context)
    else: 
        form = UserCreationForm(request.POST) 
        errors = form.errors
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/register")
        else: 
            new_user = form.save(commit=False)
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            if first_name:
                new_user.first_name = first_name  
            if last_name:
                new_user.last_name = last_name
            if email:
                new_user.email = email
            new_user.save()
            customer = Customer(user=new_user, username=new_user.username)
            customer.save()

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)

            auth_login(request, user)
            return redirect("/home")

@login_required
def home(request):
    return render(request, "home.html")

@login_required
def list_exercises(request):
    customer = request.user.customer
    exercises = customer.get_all_exercises()
    context = {'exercises': exercises}
    return render(request, "list_exercises.html", context)

@login_required
def add(request):
    return render(request, "add.html")

@login_required
def create_exercise(request):
    if request.method == "GET":
        form = CreateExerciseForm()
        context = { "form": form }
        return render(request, "create_exercise.html", context)
    else:   
        form = CreateExerciseForm(request.POST)
        new_exercise = form.extract()   
        if not new_exercise:
            errors = form.errors
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/add/create_exercise") 
        new_exercise.user = request.user
        new_exercise.save()
        return redirect("/list_exercises")

@login_required
def logout(request):
    auth_logout(request)
    return redirect('/login')

@login_required
def help(request):
    return render(request, "help.html")