from django.db import models

# Create your models here.
class Feedback(models.Model):

    ip_addr = models.GenericIPAddressField(protocol='both') # This is the only thing that we can track with the account identity and feedback reports
    
    title = models.CharField(max_length=200,verbose_name="Title")
    desc = models.CharField(max_length=400, verbose_name="Description")

    date_created = models.DateTimeField(auto_now_add=True)

    viewed = models.BooleanField(default=False)
    time_viewed = models.TimeField(auto_now=True)