from django.shortcuts import render
from django.http import HttpResponse
from .models import Service , Appointments, Pets
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# from django.contrib.auth.decorators import login_required

# from django.contrib.auth.mixins import LoginRequiredMixin 

# Create your views here.
def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})

def services_detail(request, service_id):
    service = Service.objects.get(id = service_id)
    return render(request, 'services/detail.html', {'service' : service})

# create appointments
class AppointmentsCreate(CreateView):
    model= Appointments
    fields= '__all__'

# view all the appointments
def my_appointments(request):
    appointments = Appointments.objects.all()
    return render(request, 'appointments/my_appointments.html', {'appointments':appointments})

# delete appointments
class AppointmentsDelete(DeleteView):
    model = Appointments
    success_url= '/myAppointments/'

# create pets
class PetsCreate(CreateView):
    models= Pets
    fields= '__all__'

# view all pets
def my_pets(request):
    pets = Pets.objects.all()
    return render(request, 'pets/my_pets.html', {'pets':pets})

# delete pets
class PetsDelete(DeleteView):
    models = Pets
    success_url= '/Pets/'

# update pets
# class PetsUpdate(LoginRequiredMixin, UpdateView):
#     model = Pets
#     fields = ['name', 'type', 'breed', 'description', 'age', 'image', 'appointments']
