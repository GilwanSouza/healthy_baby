from django.contrib import admin
from .models import Gestante, CustomUser

@admin.register(Gestante)
class GestanteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Gestante._meta.fields]

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomUser._meta.fields]
