from django.contrib import admin
from .models import Service, Pets, Profile

# Register your models here.
admin.site.register(Service)
admin.site.register(Pets)
admin.site.register(Profile)
