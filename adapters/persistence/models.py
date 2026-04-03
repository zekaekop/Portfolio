from django.db import models

# Create your models here.
class Anon(models.Model):
    ip_addr = models.GenericIPAddressField(protocol='both')

    name = models.CharField(max_length=200,verbose_name="Name")
    desc = models.CharField(max_length=400, verbose_name="Description")

    account_created_date = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now=True)

# FAQ = Frequently Asked Question

# Create your models here.
class FAQuestions(models.Model):
    anon = models.ForeignKey('anon', on_delete=models.CASCADE)

    question = models.TextField(null=False, blank=False)
    desc = models.CharField(max_length=600 ,null=True, blank=True)
    answer = models.TextField(null=True, blank=False)

    created_date = models.DateTimeField(auto_now_add=True)
    answered_date = models.DateTimeField(null=True)

    # The server will check every 1 hour to see if it has passed the deletion date for it to be deleted
    # possible length for the archived questions should maybe be 30 days?
    deletion_date = models.DateTimeField(null=True)

# Create your models here.
class Feedback(models.Model):

    anon = models.ForeignKey(Anon, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200,verbose_name="Title", blank=False, null=False)
    desc = models.CharField(max_length=400, verbose_name="Description",  blank=False, null=False)

    date_created = models.DateTimeField(auto_now_add=True)

    viewed = models.BooleanField(default=False)
    time_viewed = models.TimeField(auto_now=True)