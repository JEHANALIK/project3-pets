from django.shortcuts import render
from django.http import HttpResponse
from .models import Service

# Create your views here.
def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})

def services_detail(request, service_id):
    service = Service.objects.get(id = service_id)
    return render(request, 'services/detail.html', {'service' : service})