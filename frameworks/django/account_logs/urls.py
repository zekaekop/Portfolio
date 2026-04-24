from django.urls import path, reverse
from adapters.web import account_logs

views = account_logs
app_name = 'account_logs'

urlpatterns = [
    path('list_user_logs/<int:user_id>/', views.list_user_logs, name="list_user_logs"),

    # path('tags/', views.tags , name="tags"),
    # path('moderators/', views.moderators , name="moderators"),
]