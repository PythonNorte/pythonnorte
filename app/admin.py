from django.contrib import admin

# Register your models here.
from app.admin_class.eventos import Evento, EventoAdmin
from app.admin_class.disertantes import Disertante, DisertanteAdmin
from app.admin_class.recursos import Recurso, RecursoAdmin
from app.admin_class.horarios_evento import HorarioEvento, HorarioEventoAdmin

admin.site.register(Evento, EventoAdmin)
admin.site.register(Disertante, DisertanteAdmin)
admin.site.register(Recurso, RecursoAdmin)
admin.site.register(HorarioEvento, HorarioEventoAdmin)