from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):
    name= models.CharField(max_length=100)
    description= models.TextField(max_length=250)
    price= models.FloatField()
    image= models.ImageField(upload_to='main_app/static/uploads', blank=True)

class Appointments(models.Model):
    date = models.DateField()
    time= models.TimeField()
    
    class Meta:
        ordering = ['-date']