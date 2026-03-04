from django.db import models

# Create your models here.
class Feedback(models.Model):
    
    name = models.CharField(max_length=200,verbose_name="Name")
    desc = models.CharField(max_length=400, verbose_name="Description")

    date_created = models.DateTimeField(auto_now_add=True)

    viewed = models.BooleanField(default=False)
    time_viewed = models.TimeField(auto_now=True)