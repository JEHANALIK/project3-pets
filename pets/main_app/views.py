from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Service , Appointments, Pets
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


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
    fields= ['time', 'date', 'pets']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# view all the appointments
def my_appointments(request):
    appointments = Appointments.objects.filter(user=request.user)
    return render(request, 'appointments/my_appointments.html', {'appointments':appointments})

def appointments_detail(request , appointment_id):
    appointment = Appointments.objects.get(id=appointment_id)
    return render(request, 'appointments/detail.html' , {'appointment':appointment})

# delete appointments
class AppointmentsDelete(DeleteView):
    model = Appointments
    success_url= '/myAppointments/'

def pets_index(request):
    pets = Pets.objects.filter(user=request.user)
    return render(request, 'pets/index.html', {'pets': pets})

def pets_detail(request, pet_id):
    pets = Pets.objects.get(id=pet_id)
    return render(request, 'pets/detail.html', {'pets': pets})


# create pets
class PetsCreate(CreateView):
    model= Pets
    fields= ['name', 'type', 'breed', 'description', 'age', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# view all pets
def my_pets(request):
    pets = Pets.objects.all()
    return render(request, 'pets/my_pets.html', {'pets':pets})

# delete pets
class PetsDelete(DeleteView):
    model = Pets
    success_url= '/pets/'

# update pets
class PetsUpdate(UpdateView):
    model = Pets
    fields = ['name', 'type', 'breed', 'description', 'age', 'image']

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)