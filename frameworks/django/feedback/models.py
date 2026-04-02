from django.db import models
from adapters.persistance.account import Anon

# Create your models here.
class Feedback(models.Model):

    anon = models.ForeignKey(Anon, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200,verbose_name="Title", blank=False, null=False)
    desc = models.CharField(max_length=400, verbose_name="Description",  blank=False, null=False)

    date_created = models.DateTimeField(auto_now_add=True)

    viewed = models.BooleanField(default=False)
    time_viewed = models.TimeField(auto_now=True)