from django.shortcuts import render
from App_6.models import Proyecto

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listado(request):
    proye = Proyecto.objects.all()
    data = {'proyec' : proye}
    return render(request, 'listado.html', data)