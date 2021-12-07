from django.db  import models

class Habitacion(models.Model):
    id              = models.AutoField(primary_key=True)
    codigo          = models.CharField(max_length = 10, unique = True)
    descripcion     = models.CharField(max_length = 300)
    disponibilidad  = models.BooleanField(default=True)
    precio          = models.IntegerField()