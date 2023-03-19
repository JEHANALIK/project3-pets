from .models import Service

def services(request):
    services_list = Service.objects.all()
    return {'services_list': services_list}