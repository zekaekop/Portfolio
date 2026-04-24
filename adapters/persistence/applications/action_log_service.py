from django.contrib.auth.models import User
from adapters.persistence.models import Anon, SiteStatistics, User, UserProfile
from adapters.persistence.repositories import DjangoLogRepository

repository = DjangoLogRepository
 
class LogAction():
    def save(self, user, log_content):
        repository.create(user, log_content)

    def delete(self, request):

        return context