from use_cases import interfaces
from adapters.persistence.models import Anon, FAQuestions, Feedback, Projects, Log
from datetime import timedelta
from django.utils import timezone

# from django.http import QueryDict

class DjangoFAQRepository(interfaces.FAQRepository):
    model = FAQuestions

    def create(self, FAQ):
        self.model.objects.create(**FAQ)
        # query_dict = QueryDict(' ', mutable=True)
        # query_dict.objects.create(FAQ)
    
    def get_or_create_anon(self, ip_addr):
        anon, created =  Anon.objects.get_or_create(ip_addr=ip_addr)
        return created

    def get_all_archives(self, request):
        Entry.objects.filter().exclude(deletion_date=timezone.now() - timedelta(days=30)).filter(deletion_date=timezone.now())

    def answer(self, archive_id, FAQ_answer):
        self.model.objects.update(id=archive_id, FAQ_answer=FAQ_answer)

    def archive(self, archive_id):
        # Adjust days of archive deletion by the popularity of the site
        self.model.objects.update(id=archive_id, deletion_date=timezone.now() + timedelta(days=30))

    def delete(self, FAQ):
        self.model.objects.delete(**FAQ)
    
    def list(self) -> list:
        return list(self.model.objects.all())

class DjangoFeedbackRepository(interfaces.FeedbackRepository):
    model = Feedback

    def create(self, feedback):
        self.model.objects.create(**feedback)

    def delete(self, feedback):
        self.model.objects.delete(**feedback)

        def list(self) -> list:
            return list(self.model.objects.all())

class DjangoProjectShowcaseRepository(interfaces.ProjectShowcaseRepository):
    model = Projects

    def create(self, project):
        self.model.objects.create(**project)

    def delete(self, project):
        self.model.objects.delete(**project)
    
    def list(self) -> list:
        return list(self.model.objects.all())

class DjangoLogRepository(interfaces.LogRepository):
    model = Log
    
    def create(self, user, log_content):
        self.model.objects.create(user_id=user.id, log_content=log_content, date_created=timezone.now())

    def delete(self, id):
        self.model.objects.delete(id=id)
    
    def list(self) -> list:
        return list(self.model.objects.all())