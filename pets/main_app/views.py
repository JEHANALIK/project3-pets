from django.shortcuts import render
from django.http import HttpResponse
from .models import Service , Appointments
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})

def services_detail(request, service_id):
    service = Service.objects.get(id = service_id)
    return render(request, 'services/detail.html', {'service' : service})

class AppointmentsCreate(CreateView):
    model= Appointments
    fields= '__all__'

# view all the appointments
def my_appointments(request):
    appointments = Appointments.objects.all()
    return render(request, 'appointments/my_appointments.html' , {'appointments':appointments})

# delete appointments
class AppointmentsDelete(DeleteView):
    model = Appointments
    success_url= '/myAppointments/'