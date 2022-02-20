from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    users = User.objects.all()
    return render(request, "index.html", {'users':users})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
