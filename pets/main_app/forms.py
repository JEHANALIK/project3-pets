from django.forms import ModelForm
<<<<<<< HEAD
from .models import Appointments
=======
from .models import Appointments , Pets , User, Service
>>>>>>> 76b160cc864fd95481a4c65df1afa30197f37beb
from django import forms

class AppointmentsForm(forms.ModelForm):
    class Meta:
        model = Appointments
<<<<<<< HEAD
        fields = ['date', 'time', 'pets']
        widgets = {'date': forms.DateInput(attrs={'class':'datepicker'})}
=======
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

    

>>>>>>> 76b160cc864fd95481a4c65df1afa30197f37beb

