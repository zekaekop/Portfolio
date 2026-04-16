from django.urls import path, reverse
from adapters.web import admin_panel

views = admin_panel
app_name = 'admin_panel'

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('projects/', views.projects , name="projects"),
    path('users/', views.users , name="users"),
    path('tags/', views.tags , name="tags"),
    path('moderators/', views.moderators , name="moderators"),
]