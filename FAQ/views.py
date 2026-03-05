from django.shortcuts import render
from .models import FAQuestions, FAQuestionsSubmissions
# Create your views here.

class FAQCards():
    def list_FAQ(request):
        questions = FAQuestions.objects.all()
        
        return render(request, "FAQ/FAQ.html", {"faq":questions} )

    def create_FAQ(request):
        if request.method == "POST":
            question, created = FAQuestions.objects.get_or_create(asked_question=request.POST.get("question"))

            if created:
                print("this question already exists")
            
            return render(request, "FAQ/")

    def delete_FAQ(request):
        pass

    def edit_FAQ(request):
        pass

    def FAQ_question_list(request):
        pass

class FAQControlPanel():
    def AAA(request):
        pass