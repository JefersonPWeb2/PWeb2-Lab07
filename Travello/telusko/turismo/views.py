from django.shortcuts import render, redirect
from .models import DestinoTuristico
from .forms import DestinoTuristicoForm

# Create your views here.
def listar_destinos(request):
    destinos = DestinoTuristico.objects.all()
    return render(request, 'listar_destinos.html', {'destinos': destinos})

def agregar_destino(request):
    if request.method == 'POST':
        form = DestinoTuristicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_destinos')
    else:
        form = DestinoTuristicoForm()
    return render(request, 'agregar_destino.html', {'form': form})

def modificar_destino(request, id):
    destino = DestinoTuristico.objects.get(id=id)
    if request.method == 'POST':
        form = DestinoTuristicoForm(request.POST, request.FILES, instance=destino)
        if form.is_valid():
            form.save()
            return redirect('listar_destinos')
    else:
        form = DestinoTuristicoForm(instance=destino)
    return render(request, 'modificar_destino.html', {'form': form})

def eliminar_destino(request, id):
    destino = DestinoTuristico.objects.get(id=id)
    if request.method == 'POST':
        destino.delete()
        return redirect('listar_destinos')
    return render(request, 'eliminar_destino.html', {'destino': destino})