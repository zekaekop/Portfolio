from django.urls import path, reverse
from .views import Account

app_name = 'account'

urlpatterns = [
    path('register/', Account.register , name="register"),
    path('login/', Account.user_login , name="login"),
    path('logout/', Account.logout , name="logout"),
]