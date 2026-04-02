from use_cases import interfaces
from adapters.persistance import models, account

class DjangoFAQRepository(interfaces.FAQRepository):
    model = models.FAQuestions

    def create(self, FAQ):
        self.model.objects.create(FAQ)

    def list(self) -> list:
        return list(self.model.objects.all())
    
    def get_or_create_anon(self, ip_addr):
        anon, created =  account.Anon.objects.get_or_create(ip_addr=ip_addr)
        return created

    # archived items should have a item before they are deleted
    # def archive(self, FAQ):
    #     self.model.objects.create(FAQ)