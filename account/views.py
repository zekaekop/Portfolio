from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.

class Account:

    def register(request):
        login_status = False
        if request.POST.method == "POST":
            
            username = request.POST.get("username")
            password = request.POST.get("password")
            repeat_password = request.POST.get("repeat_password")

            return render(request, "/", {"login_status": status})
        return render(request, "/", {"login_status": status})


    def login(request):
        if request.POST.method == "POST":
            
            username = request.POST.get("username")
            password = request.POST.get("password")

    def logout(request):
        logout(request)
        redirect("account/login")