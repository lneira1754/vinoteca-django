from django.contrib import admin
from .models import Vino, Bodega

@admin.register(Vino)
class VinoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'precio', 'bodega')
    list_filter = ('tipo', 'bodega')
    search_fields = ('nombre',)

@admin.register(Bodega)
class BodegaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion')
    search_fields = ('nombre',)
