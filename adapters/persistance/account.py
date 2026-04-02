from django.db import models

# Create your models here.
class Anon(models.Model):
    ip_addr = models.GenericIPAddressField(protocol='both')

    name = models.CharField(max_length=200,verbose_name="Name")
    desc = models.CharField(max_length=400, verbose_name="Description")

    account_created_date = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now=True)