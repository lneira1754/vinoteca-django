from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPersonalizado

@admin.register(UsuarioPersonalizado)
class UsuarioPersonalizadoAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información Personalizada', {'fields': ('dni', 'telefono', 'direccion', 'foto_perfil')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información Personalizada', {'fields': ('dni', 'telefono', 'direccion', 'foto_perfil')}),
    )
    list_display = UserAdmin.list_display + ('dni', 'telefono')
