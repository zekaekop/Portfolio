from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Anon(models.Model):
    ip_addr = models.GenericIPAddressField(protocol='both')

    name = models.CharField(max_length=200,verbose_name="Name")
    desc = models.CharField(max_length=400, verbose_name="Description")

    activity_status = models.BooleanField(default=False)

    account_created_date = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    activity_status = models.BooleanField(default=False)
    account_created_date = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now_add=True)

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
    time_viewed = models.TimeField(auto_now_add=True)

class Projects(models.Model):

    #optional
    image = models.ImageField(upload_to="project_img" ,blank=True, null=True)
    # its optional since if the title matches a repository it will link to there if github url is emty
    github_url = models.CharField(max_length=200, verbose_name="GitHub Url", blank=True, null=True)

    title = models.CharField(max_length=200,verbose_name="Title", blank=False, null=False)
    desc = models.CharField(max_length=400, verbose_name="Description",  blank=False, null=False)
  
    uploaded_date = models.DateTimeField(auto_now_add=True)

class Log(models.Model):

    log_content = models.CharField(max_length=200, verbose_name="Log Contents", blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)

# Every day we could save and create a new row, this allows us to see daily usage that could be turned into monthly usage or yearly etc.
class SiteStatistics(models.Model):

    currently_online_user_count = models.PositiveIntegerField(default=0)
    currently_offline_user_count = models.PositiveIntegerField(default=0)

    total_anon_user_count = models.PositiveIntegerField(default=0)
    currently_online_anon_count = models.PositiveIntegerField(default=0)

    registered_user_count = models.PositiveIntegerField(default=0)

    # its small because no way we will have more than 32,767 admins / active and offline
    currently_online_admin_count = models.SmallIntegerField(default=0)
    currently_offline_admin_count = models.SmallIntegerField(default=0)