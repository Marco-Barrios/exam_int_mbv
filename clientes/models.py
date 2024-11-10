from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    DNI=models.CharField(max_length=8,default='00000000')