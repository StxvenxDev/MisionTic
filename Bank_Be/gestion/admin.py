from django.contrib import admin
'''
from .models.user import User
from .models.account import Account
admin.site.register(User)
admin.site.register(Account)'''

from .models import *

admin.site.register(Cliente)
admin.site.register(Receptor)
admin.site.register(Paquete)
admin.site.register(Envio)
admin.site.register(Factura)
# Register your models here.
