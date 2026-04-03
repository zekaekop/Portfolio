from use_cases import interfaces
from adapters.persistence.models import Anon, FAQuestions
from datetime import timedelta

# from django.http import QueryDict

class DjangoFAQRepository(interfaces.FAQRepository):
    model = FAQuestions

    def create(self, FAQ):
        self.model.objects.create(**FAQ)
        # query_dict = QueryDict(' ', mutable=True)
        # query_dict.objects.create(FAQ)

    def list(self) -> list:
        try:
            return list(self.model.objects.all())
        except self.model.DoesNotExist:
            return None
    
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
        self.model.objects.delete(FAQ)