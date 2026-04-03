from django.db import models
from adapters.persistence.models import Anon

# Create your models here.
class Message(models.Model):
    anon = models.OneToOneField(Anon, on_delete=models.CASCADE)

    message = models.CharField(max_length=200,verbose_name="Name")
    created_date = models.DateTimeField(auto_now_add=True)