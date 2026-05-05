from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.VinoListView.as_view(), name='catalogo'),
    path('vino/nuevo/', views.VinoCreateView.as_view(), name='vino_create'),
    path('vino/<int:pk>/editar/', views.VinoUpdateView.as_view(), name='vino_update'),
    path('vino/<int:pk>/eliminar/', views.VinoDeleteView.as_view(), name='vino_delete'),
]
