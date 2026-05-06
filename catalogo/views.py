from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Vino
from .forms import VinoForm

def index(request):
    return render(request, 'catalogo/index.html')

class VinoListView(ListView):
    model = Vino
    template_name = 'catalogo/catalogo.html'
    context_object_name = 'vinos'

def vino_create(request):
    if request.method == 'POST':
        form = VinoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo:catalogo')
        else:
            return redirect('catalogo:vino_create')
    else:
        form = VinoForm()
    return render(request, 'catalogo/vino_form.html', {'form': form})

def vino_update(request, id):
    vino = get_object_or_404(Vino, id=id)
    if request.method == 'POST':
        form = VinoForm(request.POST, instance=vino)
        if form.is_valid():
            form.save()
            return redirect('catalogo:catalogo')
        else:
            return redirect('catalogo:vino_update', id=id)
    else:
        form = VinoForm(instance=vino)
    return render(request, 'catalogo/vino_form.html', {'form': form})

def vino_delete(request, id):
    vino = get_object_or_404(Vino, id=id)
    if request.method == 'POST':
        vino.delete()
        return redirect(Vino)
    return render(request, 'catalogo/vino_confirm_delete.html', {'vino': vino})