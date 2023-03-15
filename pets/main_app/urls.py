from django.urls import path
from . import views

urlpatterns = [
    #R outes in express , urls in django
    path('', views.home , name='home')
]