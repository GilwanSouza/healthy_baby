from django.contrib import admin
from .models import Gestante

@admin.register(Gestante)
class GestanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'idade_gestacional', 'data_prevista_parto')
