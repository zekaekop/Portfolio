from django.db import models
from account.models import Anon

# Create your models here.
class FAQuestions(models.Model):
    anon = models.OneToOneField(Anon, on_delete=models.CASCADE)

    asked_question = models.TextField(null=False, blank=False)
    answer = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

class FAQuestionsSubmissions(models.Model):
    anon = models.OneToOneField(Anon, on_delete=models.CASCADE)

    question = models.TextField(null=False, blank=False)
    desc = models.CharField(max_length=600 ,null=False, blank=False)

    created_date = models.DateTimeField(auto_now_add=True)