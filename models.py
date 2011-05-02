from django.db import models

class Historia(models.model):
      FechaCreacion = models.DateTimeField(auto_now_add=True)       
      Abierto=models.BooleanField(default=True)

class Fragmento(models.model):
      Contenido = models.TextField()  
      Fecha = models.DateTimeField(auto_now_add=True)
