from django.contrib import admin
from .models import Gestante, CustomUser, PosParto, Odonto, Consulta

@admin.register(Gestante)
class GestanteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Gestante._meta.fields]

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomUser._meta.fields]

@admin.register(PosParto)
class PosPartoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PosParto._meta.fields]
    
@admin.register(Odonto)
class OdontoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Odonto._meta.fields]

@admin.register(Consulta)
class CosultaForm(admin.ModelAdmin):
    list_display = [field.name for field in Consulta._meta.fields]