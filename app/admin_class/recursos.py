from django.contrib import admin
from app.models.recursos import Recurso


class RecursoAdmin(admin.ModelAdmin):
    model = Recurso