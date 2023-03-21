import logging
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Service , Appointments, Pets, Reviews
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

# IMPORT FORMS
from .forms import AppointmentsForm, ReviewForm
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdateProfileForm


# Create your views here.
def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})

def services_detail(request, service_id):
    service = Service.objects.get(id = service_id)
    rest_service = Service.objects.exclude(id = service_id)
    review = Reviews.objects.filter(id = service_id)
    form = ReviewForm()
    return render(request, 'services/detail.html', {'service' : service, 'rest_service' : rest_service, 'review': review, 'form': form})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('users-profile')
    success_message = "Successfully Changed Your Password!"
    

# create appointments
class AppointmentsCreate(SuccessMessageMixin, CreateView):
    model= Appointments
    # form_class= AppointmentsForm
    fields= ['time', 'date']
    success_url = reverse_lazy('appointments_create')
    success_message = "Your appointment is successfully created!"
    # def get_form(self, *args, **kwargs):
    #     print('saad')
    #     form = super(AppointmentsCreate, self).get_form(*args, **kwargs)
    #         # so in the GET.   Limit choices queryset.
    #     form.pets = Pets.objects.get(user_id = self.request.user.id)
    #     print("pets", form.pets)
    #     form['pets'].queryset = Pets.objects.filter(user_id =self.request.user.id)
    #     print(form)
    #     return form

    def get_context_data(self, **kwargs):
        # print("khan")
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["pets"] = user.pets_set.all()
        # print("context", context)
        return context
    
    # def get_service_data(self, **kwargs):
    #     # print("khan")
    #     service = super().get_service_data(**kwargs)
    #     s = self.request.service
    #     s["services"] = s.services_set.all()
    #     # print("context", context)
    #     return s       
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.pets_id = self.request.POST['pets']
        form.instance.service_id = self.request.POST['services']
        # form.instance.services_id = self.request.POST['services']
        print("pets", self.request.POST['pets'])
        return super().form_valid(form)
        
    # def get_form_kwargs(self):
    #     kwargs = super(AppointmentsCreate, self).get_form_kwargs()
    #     kwargs['pets'] = self.request.user
    #     return kwargs

    # def get_queryset(self):
    #     pets = Pets.objects.filter(user=self.request.user)
    #     print("pets", pets)
    #     return pets

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
    success_url = reverse_lazy('my_appointments')
    success_message = "Your appointment is successfully deleted!"

def pets_index(request):
    pets = Pets.objects.filter(user=request.user)
    return render(request, 'pets/index.html', {'pets': pets})

def pets_detail(request, pet_id):
    pets = Pets.objects.get(id=pet_id)
    return render(request, 'pets/detail.html', {'pets': pets})


# create pets
class PetsCreate(SuccessMessageMixin, CreateView):
    model= Pets
    # form_class = PetsForm
    fields= ['name', 'type', 'breed', 'description', 'age', 'image']
    success_url = reverse_lazy('pets_create')
    success_message = "Pet successfully created!"


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
    # success_url= '/pets/'
    success_url = reverse_lazy('pets_index')
    success_message = "Pet successfully deleted!"

# update pets
class PetsUpdate(UpdateView):
    model = Pets
    fields = ['name', 'type', 'breed', 'description', 'age', 'image']
    success_url = reverse_lazy('pets_detail')
    success_message = "Pet successfully updated!"

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have successfully signed up!!!')
            return redirect('users-profile')
        else:
            messages.error(request, 'Invalid sign up - try again')
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated sucessfully!')
            return redirect(to='users-profile')
        else:
            messages.error(request, 'An error occured!')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

def add_review(request, service_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.service_id = service_id
        new_review.user = request.user
        new_review.save()
        print(new_review)
    return redirect('detail', service_id=service_id)