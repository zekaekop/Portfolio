from django.urls import path, reverse
from adapters.web import account

app_name = 'account'

urlpatterns = [
    path('register/', account.register , name="register"),
    path('login/', account.login , name="login"),
    path('logout/', account.logout , name="logout"),
]