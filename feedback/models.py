from django.db import models
from account.models import Anon

# Create your models here.
class Feedback(models.Model):

    anon = models.OneToOneField(Anon, on_delete=models.CASCADE) 
    
    title = models.CharField(max_length=200,verbose_name="Title")
    desc = models.CharField(max_length=400, verbose_name="Description")

    date_created = models.DateTimeField(auto_now_add=True)

    viewed = models.BooleanField(default=False)
    time_viewed = models.TimeField(auto_now=True)