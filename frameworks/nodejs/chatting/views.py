from django.shortcuts import render
from frameworks.nodejs.chatting.models import Message
from django.http import JsonResponse
import json

# Create your views here.

def save_message(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Message.objects.create(
            message=data["message"],
            created_date=data["created_date"],
        )
    return JsonResponse(data)

def chat(request):
    context = {
        "test": "hello",
    }
    return render(request, "chatting/chat.html", context)