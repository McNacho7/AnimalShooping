from urllib.parse import urlparse
from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('comidaGato', comidagatoViewset)
router.register('comidaPerro', comidaperroViewset)
router.register('accesorios', accesorioViewset)




urlpatterns = [
   path('', index,name="index") ,
   path('gatos/', gatos,name="gatos"),
   path('accesorios/', accesorios,name="accesorios"), 
   path('formulariocontacto/', formulariocontacto,name="formulariocontacto"), #se modifico nombre va sin el "-"
   path('login/', login,name="login"),
   path('mostrarperros/', mostrarperros,name="mostrarperros"),
   path('perros/', perros,name="perros"),
   path('listarproductos/', listarproductos,name="listarproductos"),
   path('listarperro/', listarperro,name="listarperro"),
   path('listaraccesorios/', listaraccesorios,name="listaraccesorios"),
   path('carro/', carro,name="carro"),
   path('form_accesorio/', form_accesorio, name="form_accesorio"),
   path('form_agregar_comida_perro/', form_agregar_comida_perro, name="form_agregar_comida_perro"),
   path('form_agregar_comida_gato/', form_agregar_comida_gato, name="form_agregar_comida_gato"),
   path('form_modi_productos/<id>/', form_modi_productos, name="form_modi_productos"),

   path('api/', include(router.urls)),
   
  
   
]