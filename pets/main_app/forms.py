from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Appointments, Profile

class AppointmentsForm(ModelForm):
    class Meta:
        model = Appointments
        fields = ['date', 'time', 'pets']

    # def __init__(self, *args, **kwargs):
    #    user = kwargs.pop('user')
    #    super(AppointmentsForm, self).__init__(*args, **kwargs)
    #    self.fields['pets'].queryset = Appointments.objects.filter(user=user)

# Update user and profile info
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UpdateProfileForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['phone']
