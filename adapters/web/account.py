from django.shortcuts import render, redirect
from adapters.persistence.applications import account_service

def register(request):
    return account_service.register(request)

def login(request):
    return account_service.user_login(request)

def logout(request):
    account_service.logout(request)
    return redirect("/account/login")