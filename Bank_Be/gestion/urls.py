


from django import views
from django.urls import path,include

from .views import ClienteApi,ReceptorApi,PaqueteApi,EnvioApi,FacturaApi
from . import views
from rest_framework import routers

apiurl = routers.SimpleRouter()
apiurl.register('clientes',ClienteApi)
apiurl.register('receptores',ReceptorApi)
apiurl.register('paquetes',PaqueteApi)
apiurl.register('envios',EnvioApi)
apiurl.register('facturas',FacturaApi)

urlpatterns = [
    path('api/',include(apiurl.urls)),
    path('',views.login,name='registro'),
    path('asignar',views.asignar,name='asignar'),
    path('registrar',views.registrar,name='registrar'),
]