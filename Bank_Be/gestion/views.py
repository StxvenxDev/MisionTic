import imp
from django.shortcuts import render
from django.http import HttpResponse




from rest_framework import serializers,viewsets
from gestion.serializers import ClienteSerializer,EnvioSerializer,FacturaSerializer,PaqueteSerializer,ReceptorSerializer
from .models.modelos import Cliente,Receptor,Paquete,Envio,Factura,Usuario

class ClienteApi(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ReceptorApi(viewsets.ModelViewSet):
    queryset = Receptor.objects.all()
    serializer_class = ReceptorSerializer

class PaqueteApi(viewsets.ModelViewSet):
    queryset = Paquete.objects.all()
    serializer_class = PaqueteSerializer

class EnvioApi(viewsets.ModelViewSet):
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer

class FacturaApi(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

def inicio(request):
    return HttpResponse("<h1>Bienvenido a Appack</h1>")

def login(request):
    return render(request,'pages/login.html')

def registrar(request):
    clientes = Cliente.objects.order_by('id')
    #salidas = '@'.join([p.nombre for p in clientes])
    context = {'lista_clientes':clientes}
    return render(request,'clientes/registrar.html',context)
def asignar(request):
    return render(request,'clientes/asignar.html')
def post_request(request):
    email = request.POST["email"]
    contraseña = request.POST["password"]
    usuario = Usuario(usuario=email,contraseña=contraseña)
    usuario.save()
    return HttpResponse(f"El usuario es {email} y la contraseña es {contraseña}")

def post_cliente(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellidos"]
    cedula = request.POST["identificacion"]
    email = request.POST["email"]
    numero = request.POST["numero"]
    direccion = request.POST["direccion"]
    cliente = Cliente(nombre=nombre,apellido=apellido,cedula=cedula,email=email,numero=numero,direccion=direccion)
    cliente.save()
    return HttpResponse(f"BIENVENIDO{nombre} {apellido}")