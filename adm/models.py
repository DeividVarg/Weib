from django.db import models
from cloudinary.models import CloudinaryField

class servicios(models.Model):
  nombre = models.CharField(max_length= 100)
  descripcion = models.TextField()
  img_prev = CloudinaryField('image', folder='servicios', null=True, blank=True)
  img_comp = CloudinaryField('image', folder='servicios', null=True, blank=True)
  
class producto(models.Model):
  nombre = models.CharField(max_length=100)
  descripcion = models.TextField()
  img_prev = CloudinaryField('image', folder='tienda', null=True, blank=True)
  img_comp = CloudinaryField('image', folder='tienda', null=True, blank=True)
  
  def __str__(self):
      return self.nombre
  
class size(models.Model):
  product = models.ForeignKey('producto', on_delete=models.CASCADE, blank=False, null=False, related_name='Tamaño')
  tamaño = models.CharField(max_length=10, null=True, blank=True)
  
  def __str__(self):
    return self.tamaño