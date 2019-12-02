from django.contrib import admin
from app.models.horarios_evento import HorarioEvento


class HorarioEventoAdmin(admin.ModelAdmin):
    model = HorarioEvento