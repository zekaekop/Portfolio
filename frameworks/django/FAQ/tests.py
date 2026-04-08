from django.test import TestCase
from adapters.persistence.models import Anon
# Create your tests here.

# unfinished

class FAQTestCase(TestCase):
    self.model.objects.create(
        repository=get_repositories()[settings.FEEDBACK_REPOSITORY],
        anon = Anon.objects.get(id=1),
        question = "How does this work?",
        answer = "This is how?",
        desc = "BLA BLA",
        created_date = "1989-01-01 00:00:01",
        answered_date = "1995-01-01 00:00:05",
        deletion_date = "2040-01-01 00:00:10",
    )

class FeedbackTestCase(TestCase):
    self.model.objects.create(
            repository=get_repositories()[settings.FEEDBACK_REPOSITORY],
            title="TItle",
            desc="description",
            # display_username="test",
            # tags = feedback_tags.BUG,
            anon = Anon.objects.get(ip_addr=get_client_ip(request)),
    )

class AccountTestCase(TestCase):
    self.model.objects.create(
        repository=get_repositories()[settings.FEEDBACK_REPOSITORY],
        anon = Anon.objects.get(id=1),
    )
    
# class FAQTestCase(TestCase):
#     self.model.objects.create(**FAQ)
    