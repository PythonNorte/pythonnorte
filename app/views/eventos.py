from django.shortcuts import render
from django.http import HttpResponse
from app.models.eventos import Evento



def view(request):
    data = {
        "eventos": Evento.objects.all(),
    }
    return render(request, 'eventos.html', data)