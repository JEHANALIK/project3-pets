from django.forms import ModelForm
from .models import Appointments

class AppointmentsForm(ModelForm):
    class Meta:
        model = Appointments
        fields = ['date', 'time', 'pets']

    # def __init__(self, *args, **kwargs):
    #    user = kwargs.pop('user')
    #    super(AppointmentsForm, self).__init__(*args, **kwargs)
    #    self.fields['pets'].queryset = Appointments.objects.filter(user=user)
