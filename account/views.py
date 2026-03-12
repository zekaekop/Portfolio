from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

class Account:

    def register(request):
        if request.method == "POST":
            
            username = request.POST.get("username")
            password = request.POST.get("password")
            repeat_password = request.POST.get("repeat_password")

            user,existing = User.objects.get_or_create(username=username)

            if (existing):
                return render(request, "account/register", { "login_status" : "Username is taken"})

            if (password == repeat_password):
                user.set_password(password)
                user.is_staff = False
                user.is_superuser = False
                user.save()
                new_user = authenticate(username=username, password=password)

                login(request, new_user)
                return render(request, "home/home.html", {"login_status": True})

            return render(request, "account/login", {"login_status": False})

    def login(request):
        if request.method == "POST":
            
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, "home/home.html", {"login_status": True})

        return render(request, "account/login.html", {"login_status": False})

    def logout(request):
        logout(request)
        return redirect("account/login")