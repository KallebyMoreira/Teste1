from django.contrib import admin
from .models import Evento,Pessoa,Pfisica,Inscrição,Ingresso

@admin.register(Evento,Pessoa,Pfisica,Inscrição,Ingresso)
class EventoAdmin(admin.ModelAdmin):
    pass

