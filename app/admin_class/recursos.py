from django.contrib import admin
from app.models.recursos import Recurso


class RecursoAdmin(admin.ModelAdmin):
    model = Recurso
    list_display = (
        'id',
        'evento',
        'nombre',
        'archivo',
    )