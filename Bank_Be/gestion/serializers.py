from curses import meta
from dataclasses import field
from rest_framework import serializers
from .models.modelos import Cliente,Receptor,Paquete,Envio,Factura

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id','nombre','apellido','cedula','email','numero','direccion')

class ReceptorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receptor
        fields = ('id','nombre','apellido','cedula','numero','direccion','cliente')

class PaqueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paquete
        fields = ('id','cliente','precio')

class EnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envio
        fields = ('id','costo','tipo','paquete')

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ('id','envio','cliente','total')

