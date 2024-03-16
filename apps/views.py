from django.http import HttpResponse
from django.shortcuts import render
from apps.models import Person


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def index(request):
    data = {}
    data["dataset"] = Person.objects.all()
    return render(request, 'index.html', data)
