from django.db import models

class Recurso(models.Model):
    evento = models.ForeignKey("Evento", related_name="recursos", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    icono = models.CharField(max_length=200, blank=True, null=True)
    archivo = models.FileField(upload_to="recursos")

    class Meta:
        db_table = "recursos"