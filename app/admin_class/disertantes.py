from django.contrib import admin
from app.models.disertantes import Disertante

class DisertanteAdmin(admin.ModelAdmin):
    model = Disertante
    list_display = (
        'id',
        'nombre',
        'apellido',
        'email',
    )
    search_fields = ('nombre', 'apellido')