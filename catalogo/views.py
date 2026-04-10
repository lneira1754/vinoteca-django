from django.http import HttpResponse
from django.shortcuts import render
from .models import Vino # Importamos el modelo

# def catalogo(request):
#     vinos = [
#         'Pinot Noir',
#         'Chardonnay',
#         'Merlot',
#         'Zinfandel',
#         'Cabernet Sauvignon']
#     return render(request, 'catalogo/catalogo.html', {'vinos': vinos})

def catalogo(request):
    vinos_db = Vino.objects.all() # Trae todos los vinos de la DB
    return render(request, 'catalogo/catalogo.html', {'vinos': vinos_db})

def index(request):
    return render(request, 'catalogo/index.html')

