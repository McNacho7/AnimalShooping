from django.db import models

class comidagatos(models.Model):
    codigo = models.CharField(max_length=11, unique=True)
    nombre = models.CharField(max_length=50)
    edad = models.CharField(max_length=2)
    raza = models.CharField(max_length=50)

class comidaperro(models.Model):
    codigo = models.CharField(max_length=11, unique=True)
    nombre = models.CharField(max_length=50)
    edad = models.CharField(max_length=2)
    raza = models.CharField(max_length=50)

class accesorio(models.Model):
    codigo = models.CharField(max_length=11, unique=True)
    nom_accesorio = models.CharField(max_length=50)
    precio = models.CharField(max_length=20)

    





