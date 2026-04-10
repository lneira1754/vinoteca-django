from django.urls import path, include
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
]