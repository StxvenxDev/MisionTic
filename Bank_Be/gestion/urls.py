


from django.urls import path,include

from .views import ClienteApi,ReceptorApi,PaqueteApi,EnvioApi,FacturaApi
from rest_framework import routers

apiurl = routers.SimpleRouter()
apiurl.register('clientes',ClienteApi)
apiurl.register('receptores',ReceptorApi)
apiurl.register('paquetes',PaqueteApi)
apiurl.register('envios',EnvioApi)
apiurl.register('facturas',FacturaApi)
urlpatterns = [
    path('api/',include(apiurl.urls))
]