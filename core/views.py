from django.shortcuts import render
from .models import comidagato, comidaperro, accesorio
from rest_framework import viewsets
from .serializers import comidagatoSerializer, comidaperroSerializer, accesorioSerializer





class comidagatoViewset(viewsets.ModelViewSet):
    queryset = comidagato.objects.all()
    serializer_class = comidagatoSerializer

class comidaperroViewset(viewsets.ModelViewSet):
    queryset = comidaperro.objects.all()
    serializer_class = comidaperroSerializer

class accesorioViewset(viewsets.ModelViewSet):
    queryset = accesorio.objects.all()
    serializer_class = accesorioSerializer




def index(request):
    return render(request, 'core/index.html')

def gatos(request):
    return render(request, 'core/gatos.html')

def accesorios(request):
    return render(request, 'core/accesorios.html')

def formulariocontacto(request):
    return render(request, 'core/formulariocontacto.html')

def login(request):
    return render(request, 'core/login.html')

def mostrarperros(request):
    return render(request, 'core/mostrarperros.html')

def perros(request):
    return render(request, 'core/perros.html')

def carro(request):
    return render(request, 'core/carro.html')

def listarproductos(request):
    comidaGA = comidagato.objects.all()
    datos ={
        'comidaGa': comidaGA
    }
    return render(request, 'core/listarproductos.html',datos)

def listarperro(request):
    comidaPERRO = comidaperro.objects.all()
    datos ={
        'comidaPERRO': comidaPERRO
    }
    return render(request, 'core/listarperro.html',datos)

def listaraccesorios(request):
    accesorios = accesorio.objects.all()
    datos ={
        'accesorio': accesorios
    }
    return render(request, 'core/listaraccesorios.html',datos)