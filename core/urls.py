from urllib.parse import urlparse
from django.urls import path, include
from .views import index, gatos, accesorios, formulariocontacto, listaraccesorios, listarperro, login, mostrarperros, perros, listarproductos, carro, comidagatoViewset, comidaperroViewset, accesorioViewset
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
   path('api/', include(router.urls)),
  
   
]