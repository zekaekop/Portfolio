from django.shortcuts import render

# Create your views here.
def report(request):
    
    content = {
        "test":"test",
    }
    
    return render(request, "feedback/feedback_form.html" , content)