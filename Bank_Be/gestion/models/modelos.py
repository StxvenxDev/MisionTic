from email.policy import default
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models

class Cliente (models.Model):
    nombre = models.CharField('Nombre',max_length=20)
    apellido = models.CharField('Apellido',max_length=20)
    cedula = models.CharField('Cedula',max_length=15,null= False)
    email = models.CharField('Email',max_length = 50)
    numero = models.CharField('Telefono',max_length=20)
    direccion = models.CharField('Direccion',max_length=15)

    def __str__(self):
        return f"ID = {self.id}"

class Usuario(models.Model):
    usuario = models.CharField('Usuario',max_length=50,null=False)
    contraseña = models.CharField('Contraseña',max_length=20,null=False)
    
class Receptor(models.Model):
    nombre = models.CharField('Nombre',max_length=20)
    apellido = models.CharField('Apellido',max_length=20)
    cedula = models.CharField('Cedula',max_length=15,null=False)
    numero = models.IntegerField('Telefono')
    direccion = models.CharField('Direccion',max_length=15)
    cliente = models.OneToOneField(Cliente,on_delete=models.CASCADE,null=False)
    
class Paquete(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,null=False)
    precio = models.DecimalField(max_digits=5, decimal_places=2,)

class Envio(models.Model):
    costo = models.DecimalField(max_digits=5, decimal_places=2,)
    tipo = models.CharField('Tipo de envio',max_length=10)
    paquete = models.ForeignKey(Paquete,on_delete=models.CASCADE,null=False)

class Factura(models.Model):
    envio = models.ForeignKey(Envio,on_delete=models.CASCADE,null=False)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=5, decimal_places=2,)
    

