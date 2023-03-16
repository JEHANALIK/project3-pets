from django.urls import path
from . import views

urlpatterns = [
    #R outes in express , urls in django
    path('', views.home , name='home'),
    path('services/<int:service_id>', views.services_detail, name='detail'),
    
]