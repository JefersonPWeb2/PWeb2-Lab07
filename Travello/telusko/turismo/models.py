from django.db import models

# Create your models here.
class DestinoTuristico(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='destinos/')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    oferta = models.BooleanField(default=False)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nombre