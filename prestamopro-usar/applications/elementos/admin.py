from django.contrib import admin
from .models import Elemento
from .models import Estado
from .models import Persona
from .models import Prestamo

# Register your models here.
admin.site.register(Elemento)
admin.site.register(Estado)
admin.site.register(Persona)
admin.site.register(Prestamo)

