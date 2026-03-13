from django.db import models
from account.models import Anon
# Create your models here.

class Post:
    original_poster = models.ForeignKey(Anon, on_delete=models.CASCADE)
    title = models.CharField(null=False, blank=False)
    desc = models.CharField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(auto_created=True)