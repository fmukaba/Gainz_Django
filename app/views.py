from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User 
from .forms import RegisterForm

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:    
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/login")
        else: 
            username = request.POST["username"] 
            password = request.POST["password"] # hash password later Bcrypt
            user = User.objects.filter(username=username)
            logged_user = user[0]
            
            if logged_user.password == password:
                request.session['userid'] = logged_user.id
                return redirect("/home")
            return redirect("/login")

def register(request):
    if request.method == "GET":
        form = RegisterForm()
        context = { "regForm": form }
        return render(request, "register.html", context)
    else:    
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/register")
        else: 
            email = request.POST["email"]
            username = request.POST["username"] 
            password = request.POST["password"] # hash password later Bcrypt
            new_user = User(email=email, username=username, password=password)
            new_user.save()
            return redirect("/home")

def home(request):
    return render(request, "home.html")

def list_users(request):
    context = {"users": User.objects.all()}
    return render(request, "list_users.html", context)