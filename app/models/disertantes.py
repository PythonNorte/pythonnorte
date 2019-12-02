from django.db import models
from mdeditor.fields import MDTextField

class Disertante(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    resumen = MDTextField(blank=True, null=True, default=None)

    class Meta:
        db_table = "disertantes"

    def __str__(self):
        return self.nombre_completo

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"