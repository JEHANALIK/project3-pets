from django.urls import path
from . import views

urlpatterns = [
    #R outes in express , urls in django
    path('', views.home , name='home'),
    path('services/<int:service_id>', views.services_detail, name='detail'),
    path('appointments/create', views.AppointmentsCreate.as_view(), name='appointments_create'),
    path('myAppointments/' , views.my_appointments , name='my_appointments'),
    path('appointments/<int:pk>/delete' , views.AppointmentsDelete.as_view(), name='appointments_delete'),
    path('appointments/<int:appointment_id>' , views.appointments_detail , name='appointments_detail'),

    path('pets/', views.pets_index, name='pets_index'),
    path('pets/create/' , views.PetsCreate.as_view() , name='pets_create'),
    path('pets/<int:pet_id>', views.pets_detail, name='pets_detail'),
    path('pets/<int:pk>/update', views.PetsUpdate.as_view(), name='pets_update'),
    path('pets/<int:pk>/delete', views.PetsDelete.as_view(), name='pets_delete'),

]