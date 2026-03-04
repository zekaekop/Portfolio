from django.shortcuts import render

# Create your views here.

def home_page(request):

    tags = ("CSS","HTML","JS","C","C++","Python","PHP","TypeScript","Bash","MySQL","GIT","Django", "Nginx", "NodeJS", )

    context = {
        "world":"World!!",
        "tags":  tags,
    }
    
    return render(request, "home/home.html", context)
