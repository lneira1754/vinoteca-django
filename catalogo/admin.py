from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Vino, Bodega, UsuarioPersonalizado

@admin.register(Vino)
class VinoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'precio', 'bodega')
    list_filter = ('tipo', 'bodega')
    search_fields = ('nombre',)

@admin.register(Bodega)
class BodegaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion')
    search_fields = ('nombre',)

@admin.register(UsuarioPersonalizado)
class UsuarioPersonalizadoAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información Personalizada', {'fields': ('dni', 'telefono', 'direccion', 'imagen_perfil')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información Personalizada', {'fields': ('dni', 'telefono', 'direccion', 'imagen_perfil')}),
    )
    list_display = UserAdmin.list_display + ('dni', 'telefono')
