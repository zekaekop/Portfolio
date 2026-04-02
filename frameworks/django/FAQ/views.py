# from django.shortcuts import render
# from .models import FAQuestions, FAQuestionsSubmissions
# from account.models import Anon
# from home.views import get_client_ip
# Create your views here.

# class FAQCards:
#     def list_FAQ(self, request):
#         FAQs = FAQuestions.objects.all()

#         FAQSubmissions.create_submissions(self, request)

#         context = {
#             "FAQs":FAQs,
#             "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
#         }
        
#         return render(request, "FAQ/FAQ.html", context )

    # def create_FAQ(self, request):
    #     if request.method == "POST":
    #         question, created = FAQuestions.objects.get_or_create(
    #             asked_question=request.POST.get("asked_question"),
    #             answer=request.POST.get("answer"),
    #             anon=Anon.objects.get(ip_addr=get_client_ip(request)))

    #         if created:
    #             print("this FAQ already exists")
    #         else:
    #             print("Working FAQ")
            
    #         context = {
    #             "status_message": created,
    #             "question": question,
    #             "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    #             "FAQSs":  FAQuestionsSubmissions.objects.all(),
    #         }

    #         return render(request, "FAQ/FAQ.html", context)

    #     context = {
    #         "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    #         "FAQSs": FAQuestionsSubmissions.objects.all(),
    #     }

    #     return render(request, "FAQ/FAQ_create.html", context)

    # def delete_FAQ(self, request):

    #     context = {
    #         "test":"hello world",
    #     }

    #     return render(request, "FAQ/FAQ_admin_panel.html", context)

    # def edit_FAQ(self, request):
    #     context = {
    #         "test":"hello world",
    #     }

    #     return render(request, "FAQ/FAQ_admin_panel.html", context)
