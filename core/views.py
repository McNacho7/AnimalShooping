from gc import get_objects
from django.shortcuts import render, redirect, get_object_or_404
from .models import comidagato, comidaperro, accesorio
from rest_framework import viewsets
from django.http import HttpResponse 
from .serializers import comidagatoSerializer, comidaperroSerializer, accesorioSerializer
from .forms import accesorioForm, agregarcomidaPerroForm,agregarcomidaGatoForm





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

def form_accesorio(request):
    data = {
        'form': accesorioForm()
    }

    if request.method == 'POST':
        formulario = accesorioForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            data['mensaje'] = "Guardados Correctamente"
        else:
            data ['form'] = formulario
    return render (request, 'core/form_accesorio.html', data)


def form_agregar_comida_perro(request):
    data = {
        'form': agregarcomidaPerroForm()
    }

    if request.method == 'POST':
        formulario = agregarcomidaPerroForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            data['mensaje'] = "Guardados Correctamente"
        else:
            data ['form'] = formulario
    return render (request, 'core/form_agregar_comida_perro.html', data)


def form_agregar_comida_gato(request):
    data = {
        'form': agregarcomidaGatoForm()
    }

    if request.method == 'POST':
        formulario = agregarcomidaGatoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            data['mensaje'] = "Guardados Correctamente"
        else:
            data ['form'] = formulario
    return render (request, 'core/form_agregar_comida_gato.html', data)


def form_modi_productos(request, id):

    accesorios =  accesorio.objects.get(idAccesorio=id)
    datos = {
        'form': accesorioForm(instance=accesorios)
    }
    if request.method == 'POST':
        formulario = accesorioForm(data=request.POST, instance=accesorios)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificado Correctamente"
            return redirect (to="listaraccesorios")
        else:
            datos ['form'] = formulario

    return render(request, 'core/form_modi_productos.html',datos)


def form_modi_perro(request, id):

    produccomidaperro = comidaperro.objects.get(idPerro=id)
    datos = {
        'form': agregarcomidaPerroForm(instance=produccomidaperro)
    }
    if request.method == 'POST':
        formulario = agregarcomidaPerroForm(data=request.POST, instance=produccomidaperro)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificado Correctamente"
            return redirect (to="listaraccesorios")
        else:
            datos ['form'] = formulario

    return render(request, 'core/form_modi_perro.html',datos)


