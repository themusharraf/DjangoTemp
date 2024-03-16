from django.http import HttpResponse


def index(request):
    return HttpResponse("Home page")


def index2(request):
    return HttpResponse("About page ")
