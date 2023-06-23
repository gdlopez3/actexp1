from django.db import models

# Create your models here.
class EntidadFinanciera(models.Model):
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)
    num_suc = models.IntegerField()
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return """Nombre: %s - Siglas: %s \n
                Num_suc: %d\n
                Ciudad: %s""" % (self.nombre,
                self.siglas,
                self.num_suc,
                self.ciudad)
                