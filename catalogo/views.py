from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Vino
from .forms import VinoForm

def index(request):
    return render(request, 'catalogo/index.html')

class VinoListView(ListView):
    model = Vino
    template_name = 'catalogo/catalogo.html'
    context_object_name = 'vinos'

class VinoCreateView(CreateView):
    model = Vino
    form_class = VinoForm
    template_name = 'catalogo/vino_form.html'
    success_url = reverse_lazy('catalogo:catalogo')

class VinoUpdateView(UpdateView):
    model = Vino
    form_class = VinoForm
    template_name = 'catalogo/vino_form.html'
    success_url = reverse_lazy('catalogo:catalogo')

class VinoDeleteView(DeleteView):
    model = Vino
    template_name = 'catalogo/vino_confirm_delete.html'
    success_url = reverse_lazy('catalogo:catalogo')
