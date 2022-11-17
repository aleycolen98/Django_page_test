from django.db import models

# Create your models here.
class Disco(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    banda = models.CharField(max_length=100)
    subgenero = models.CharField(max_length=100)
    anio = models.IntegerField
    imagen = models.ImageField(upload_to='images/', null=True, verbose_name="Imagen")

    def __str__(self):
        nombre_admin = self.nombre + " by " + self.banda 
        return nombre_admin

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()