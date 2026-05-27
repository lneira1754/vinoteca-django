from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.vinos, name='catalogo'),
    path('vino/nuevo/', views.vino_create, name='vino_create'),
    path('vino/<int:id>/editar/', views.vino_update, name='vino_update'),
    path('vino/<int:id>/eliminar/', views.vino_delete, name='vino_delete'),
]
