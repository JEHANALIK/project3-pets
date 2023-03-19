from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.

class Service(models.Model):
    name= models.CharField(max_length=100)
    description= models.TextField(max_length=250)
    price= models.FloatField()
    image= models.ImageField(upload_to='main_app/static/uploads', blank=True)

class Pets(models.Model):

    class PetType(models.TextChoices):
        dog = 'D', _('Dog')
        cat = 'C' , _('Cat')
        

    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length = 2,
        choices = PetType.choices,
        # default = PetType.dog
     )
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='main_app/static/uploads', blank=True)
    # appointments = models.ForeignKey(Appointments, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pets_detail", kwargs={"pet_id": self.id})
    


class Appointments(models.Model):
    date = models.DateField()
    time= models.TimeField()
    pets = models.ForeignKey(Pets, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-date']

    

    def get_absolute_url(self):
        return reverse("appointments_detail", kwargs={"appointment_id": self.id})

# TYPES = [
#     ('C', 'Cat'),
#     ('D', 'Dog')
# ]

