from django.shortcuts import render
from .models import FAQuestions, FAQuestionsSubmissions
from account.models import Anon
from home.views import get_client_ip
# Create your views here.

class FAQCards():
    def list_FAQ(self, request):
        FAQs = FAQuestions.objects.all()

        context = {
            "FAQs":FAQs,
            "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
        }
        
        return render(request, "FAQ/FAQ.html", context )

    def create_FAQ(self, request):
        if request.method == "POST":
            question, created = FAQuestions.objects.get_or_create(asked_question=request.POST.get("question"))

            if created:
                print("this FAQ already exists")
            else:
                print("Working FAQ")
            
            context = {
                "status_message": created,
                "question": question,
                "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
            }

            return render(request, "FAQ/FAQ_create.html", context)

    def delete_FAQ(self, request):

        context = {
            "test":"hello world",
        }

        return render(request, "FAQ/FAQ_admin_panel.html", context)

    def edit_FAQ(self, request):
        context = {
            "test":"hello world",
        }

        return render(request, "FAQ/FAQ_admin_panel.html", context)

    def FAQ_submissions_list(self, request):
        pass

class FAQSubmissions():
    def create_submissions(self, request):
        if request.method == "POST":

            # create the submission
            submission, created = FAQuestionsSubmissions.objects.get_or_create(
                question=request.POST.get("question"),
                desc=request.POST.get("desc"),
                anon=Anon.objects.get(ip_addr=get_client_ip(request)))

            if created:
                print("this submission already exists")
            else:
                print("Working Submission")
            
            context = {
                "status_message": created,
                "submission": submission,
                "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
            }

            return render(request, "FAQ/FAQ.html", context)