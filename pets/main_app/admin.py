from django.contrib import admin
from .models import Service, Pets, Profile, Reviews

# Register your models here.
admin.site.register(Service)
admin.site.register(Pets)
admin.site.register(Profile)
admin.site.register(Reviews)
