from django.db import models


class HorarioEvento(models.Model):
    evento = models.ForeignKey("Evento", related_name="horarios", on_delete=models.CASCADE)
    fecha = models.DateField()
    inicio = models.TimeField()
    fin = models.TimeField()

    class Meta:
        db_table = "horarios_evento"
        verbose_name_plural = "Horarios de los Eventos"

    def __str__(self):
        return self.evento.titulo + " - " + self.fecha.strftime("%d/%m/%Y")