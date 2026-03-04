from django.shortcuts import render

# Create your views here.

def home_page(request):

    frameworks = ("Django", "Nginx", "NodeJS", ) # ETC.
    tags = ("CSS","HTML","JS","C","C++","Python","PHP",)

    context = {
        "world":"World!!",
        "tags":  tags,
        "frameworks": frameworks,
    }
    
    return render(request, "home/home.html", context)
