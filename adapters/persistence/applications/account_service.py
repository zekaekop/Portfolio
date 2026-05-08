from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from adapters.persistence.models import UserProfile
from adapters.persistence.applications.action_log_service import  LogAction

# Create your views here.

# The reason why the functions are called user_register etc. 
# Is because function names were conflicting with django.contrib.auth import login name

def user_register(request):
    if request.method == "POST":
        
        username = request.POST.get("username") 
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")


        # i dont know, dont question it
        # if (user_profile_existing):
        #     return render(request, "account/register.html", { "login_status" : "Account User Profile Already Exists"})

        if (password == repeat_password): 

            if (User.objects.filter(username=username).exists()):
                return render(request, "account/register.html", { "login_status" : "Account username is taken"})

            user = User.objects.create_user(username=username, password=password, is_staff=False, is_superuser=False)
            UserProfile.objects.create(user=user)

            LogAction().log_user_registered(user)

            user.save()
            new_user = authenticate(username=username, password=password)

            login(request, new_user)
            return redirect("/")

    return render(request, "account/register.html", {"login_status": False})

def user_login(request):
    if request.method == "POST":
        
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            UserProfile.objects.get_or_create(user=user)
            LogAction().log_user_login(user)

            login(request, user)
            return redirect("/")
        else:
            return render(request, "account/login.html", {"login_status": "User does not exist"})

    return render(request, "account/login.html")

def user_logout(request):
    LogAction().log_user_logout(request)
    logout(request)
    return redirect("account/login")