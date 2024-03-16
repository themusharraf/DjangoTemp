from django.urls import path
from apps.views import index, index2

urlpatterns = [
    path('home', index, name='index'),
    path('about', index2, name='about')
]
