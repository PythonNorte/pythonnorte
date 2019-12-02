from django.contrib import admin
from app.models.eventos import Evento
from app.models.horarios_evento import HorarioEvento
from app.models.recursos import Recurso

class RecursosInline(admin.TabularInline):
    model = Recurso

class HorariosEventoInline(admin.TabularInline):
    model = HorarioEvento

class EventoAdmin(admin.ModelAdmin):
    model = Evento
    list_display = (
        'id',
        'titulo',
        'tipo',
        'disertantes_',
    )
    search_fields = ('titulo', )
    autocomplete_fields = ['disertantes', ]
    inlines = [
        HorariosEventoInline,
        RecursosInline,
    ]