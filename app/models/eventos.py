from django.db import models
from mdeditor.fields import MDTextField

TIPOS = (
    ('CHARLA', 'CHARLA'),
    ('TALLER', 'TALLER'),
    ('CURSO', 'CURSO'),
    ('OTRO', 'OTRO'),
)

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = MDTextField(blank=True, null=True, default=None)
    temario = MDTextField(blank=True, null=True, default=None)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    disertantes = models.ManyToManyField("Disertante")
    publicar = models.BooleanField(default=True)
    pueden_inscribirse = models.BooleanField(default=False)
    inscripcion_abierta = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "eventos"

    def __str__(self):
        return self.titulo

    def disertantes_(self):
        return ", ".join([d.nombre_completo for d in self.disertantes.all()])