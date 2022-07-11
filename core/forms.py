from dataclasses import field
from pyexpat import model
from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import accesorio,comidagato,comidaperro

class accesorioForm(forms.ModelForm):
    class Meta:
        model = accesorio
        fields = '__all__'

class agregarcomidaPerroForm(forms.ModelForm):
    class Meta:
        model = comidaperro
        fields = '__all__'

class agregarcomidaGatoForm(forms.ModelForm):
    class Meta:
        model = comidagato
        fields = '__all__'