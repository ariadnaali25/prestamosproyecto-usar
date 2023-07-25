from django.shortcuts import render
from django.db import models



class Elemento(models.Model):
    detalle_elemento = models.CharField("Elemento", max_length=50)
    def __str__(self):
        return str(self.id)+'-'+self.detalle_elemento
    

class Estado(models.Model):
    detalle_estado = models.CharField("Estado", max_length=50)
    def __str__(self):
        return str(self.id)+'-'+self.detalle_estado
    

class Persona(models.Model):
    nombre = models.CharField("Nombre", max_length=50, default="")
    telefono=models.CharField("Telefono", max_length=20,default="")
    mail=models.CharField("Mail", max_length=60, default="")
    def __str__(self):
        return str(self.id)+'-'+self.nombre
   
    

class Prestamo(models.Model):
    fecha = models.CharField("Fecha de prestamo", max_length=15)
    fechaposdev=models.CharField("Fecha posible de devolucion", max_length=15)
    fechadev=models.CharField("Fecha de devolucion", max_length=15 )
    elemento=models.ForeignKey(Elemento, on_delete=models.CASCADE)
    deudor=models.ForeignKey(Persona, on_delete=models.CASCADE)
    estado=models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+'-'+self.fecha