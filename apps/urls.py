from django.urls import path
from apps.views import home, about,index

urlpatterns = [
    path('home', home, name='home'),
    path('about', about, name='about'),
    path('', index, name='index')
]
