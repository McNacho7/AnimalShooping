from django.contrib import admin
from .models import comidagatos, comidaperro, accesorio

# Register your models here.

admin.site.register(comidagatos)
admin.site.register(comidaperro)
admin.site.register(accesorio)