from django.forms import ModelForm
from .models import Appointments

class AppointmentsForm(ModelForm):
    class Meta:
        model = Appointments
        fields = ['date', 'time']

