from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from django.contrib.auth.models import User
from django_login_history.models import Login
from django.utils.timezone import now

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    users = User.objects.all()
    times = Login.objects.filter(user=request.user).count
    year, week, day = now().isocalendar()
    today = Login.objects.filter(date__day=now().day).values("user").distinct().count
    week = Login.objects.filter(date__week=week).values("user").distinct().count
    return render(request, "index.html", {'users':users, 'times':times, 'today':today, 'week':week})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
