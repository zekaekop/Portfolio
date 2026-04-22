from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from adapters.persistence.models import Anon, SiteStatistics, User, UserProfile
# Create your views here.

def fetch_stats(request):
    if request.method == "POST":
        # TODO: Refresh button
        pass

    context = {
        "currently_online_user_count": SiteStatistics.objects.get(),
        "currently_offline_user_count": SiteStatistics.objects.count(),
        
        "total_anon_user_count": SiteStatistics.objects.count(),
        "currently_online_anon_count": SiteStatistics.objects.count(),

        "registered_user_count": SiteStatistics.objects.count(),

        "currently_online_admin_count": SiteStatistics.objects.count(),
        "currently_offline_admin_count": SiteStatistics.objects.count(),
    }

    return context

def set_stats(request):

    data = {
        "currently_online_user_count": UserProfile.objects.filter(activity_status=True).all().count(),
        "currently_offline_user_count": UserProfile.objects.filter(activity_status=False).count(),
        
        "total_anon_user_count": Anon.objects.count(),
        "currently_online_anon_user_count": Anon.objects.filter(activity_status=True).count(),

        "registered_user_count": User.objects.count(),

        # "currently_online_admin_count": UserProfile.objects.filter(role="admin", activity_status=True).count(),
        # "currently_offline_admin_count": UserProfile.objects.filter(role="admin", activity_status=False).count(),
    }

    sitestatistics, create = SiteStatistics.objects.get_or_create(
        currently_online_user_count=data["currently_online_user_count"],
        currently_offline_user_count=data["currently_offline_user_count"],

        total_anon_user_count=data["total_anon_user_count"],
        currently_online_anon_user_count=data["currently_online_anon_user_count"],

        registered_user_count=data["registered_user_count"],

        # currently_online_admin_count=data["currently_online_admin_count"],
        # currently_offline_admin_count=data["currently_offline_admin_count"],
        )

    if create:
        print("Failed to set and create site statistics")

    return data

