from django.forms import ModelForm
from .models import Appointments , Pets , User, Service
from django import forms

class AppointmentsForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['date', 'time']

        widgets= {
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'class': 'form-control'}),
        }

class PetsForm(forms.ModelForm):
    class Meta:
        model: Pets
        fields = ['name','type','breed','age','description']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'type': forms.Select(attrs={'class':'form-control'}),
            'breed': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }

    


