from django.shortcuts import render, redirect, get_object_or_404
from .models import Vino
from .forms import VinoForm

def index(request):
    return render(request, 'catalogo/index.html')
#metodo
def vinos(request):
    vinos = Vino.objects.all()
    return render(request, 'catalogo/catalogo.html', {'vinos':vinos})    

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
        return redirect('catalogo:catalogo')
    return render(request, 'catalogo/vino_confirm_delete.html', {'vino': vino})