from django.urls import path
from apps.views import home, about

urlpatterns = [
    path('home', home, name='index'),
    path('about', about, name='about')
]
