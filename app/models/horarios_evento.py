from django.db import models


class HorarioEvento(models.Model):
    evento = models.ForeignKey("Evento", related_name="horarios", on_delete=models.CASCADE)
    fecha = models.DateField()
    inicio = models.TimeField()
    fin = models.TimeField()

    class Meta:
        db_table = "horarios_evento"