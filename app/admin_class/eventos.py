from django.contrib import admin
from app.models.eventos import Evento


class EventoAdmin(admin.ModelAdmin):
    model = Evento
    list_display = (
        'titulo',
        'tipo',
        'disertantes_',
    )
    search_fields = ('titulo', )
    autocomplete_fields = ['disertantes', ]