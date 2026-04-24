from django.contrib.auth.models import User
from adapters.persistence.models import Anon, SiteStatistics, User, UserProfile
from adapters.persistence.repositories import DjangoLogRepository

repository = DjangoLogRepository()
 
class LogAction():

    # def log_faq_create(self, status, user, question_id):
    #     log_content = f"User {user.username} created a question in FAQ (Question ID: {question_id})"
    #     self.save(user, log_content)

    # def log_admin_panel_access(self, status, user):
    #     log_content = f"User {user.username} accessed admin panel"
    #     self.save(user, log_content)

    def log_user_logout(self, request):
        user = User.objects.get(id=request.user.id)
        log_content = f"User {user.username} logged out"
        self.save(user, log_content)

    def log_user_login(self, user):
        log_content = f"User {user.username} logged in"
        self.save(user, log_content)

    def log_user_registered(self, user):
        log_content = f"User {user.username} registered"
        self.save(user, log_content)

    # See user_status_consumer.py for better understanding
    def log_user_status(self, model, status, user):
        current_status = model.objects.get(user_id=user.pk).activity_status

        if current_status == status:
            return None

        if status == False:
            log_content = f"User Status: {user.username} is offline"
        else:
            log_content = f"User Status: {user.username} is online"

        self.save(user, log_content)

    def save(self, user, log_content):
        repository.create(user, log_content)

    # def delete(self, request):
    #     return context