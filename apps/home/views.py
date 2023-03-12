from django.shortcuts import render
from .models import Client
from .models import Service

# Create your views here.
def index(request):
    client1 = Client()
    client1.id = 0
    client1.name = 'Ideax'
    client1.img = '/static/images/icons/clients/ideax.svg'

    client2 = Client()
    client2.id = 1
    client2.name = 'Alfamart'
    client2.img = '/static/images/icons/clients/alfamart.svg'

    client3 = Client()
    client3.id = 2
    client3.name = 'Filantropi'
    client3.img = '/static/images/icons/clients/filantropi.svg'

    clients = [client1, client2, client3]

    services = Service.objects.all()

    return render(request, 'index.html', {'clients': clients, 'services': services})