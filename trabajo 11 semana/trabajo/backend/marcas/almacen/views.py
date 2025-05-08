from django.shortcuts import render, redirect, get_object_or_404
from .forms import PrendaForm
from .models import Prenda

# Vista de inicio
def inicio(request):
    """Muestra la página de inicio."""
    return render(request, 'index.html')

# Vista para registrar una nueva prenda
def registrar_prenda(request):
    """
    Muestra un formulario para registrar una prenda.
    Si se envía por POST y es válido, guarda la prenda y redirige a éxito.
    """
    if request.method == 'POST':
        form = PrendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')
    else:
        form = PrendaForm()
    return render(request, 'registrar_prenda.html', {'form': form})

# Vista que confirma el registro exitoso
def registro_exitoso(request):
    """Muestra una página de confirmación tras registrar una prenda."""
    return render(request, 'registro_exitoso.html')

# Vista que lista todas las prendas registradas
def lista_prendas(request):
    """Muestra una lista de todas las prendas en la base de datos."""
    prendas = Prenda.objects.all()
    return render(request, 'lista_prendas.html', {'prendas': prendas})

# Vista para buscar una prenda por ID
def buscar_prenda(request):
    """
    Permite buscar una prenda por su ID usando una consulta GET.
    Muestra los datos de la prenda si se encuentra.
    """
    prenda = None
    prenda_id = request.GET.get('prenda_id')
    if prenda_id:
        try:
            prenda = Prenda.objects.get(id=prenda_id)
        except Prenda.DoesNotExist:
            prenda = None
    return render(request, 'buscar_prenda.html', {'prenda': prenda, 'prenda_id': prenda_id})

# Vista para actualizar los datos de una prenda existente
def actualizar_prenda(request, prenda_id):
    """
    Permite actualizar los datos de una prenda existente mediante un formulario.
    Redirige a la lista de prendas después de guardar los cambios.
    """
    prenda = get_object_or_404(Prenda, id=prenda_id)
    if request.method == 'POST':
        form = PrendaForm(request.POST, instance=prenda)
        if form.is_valid():
            form.save()
            return redirect('lista_prendas')
    else:
        form = PrendaForm(instance=prenda)
    return render(request, 'actualizar_prenda.html', {'form': form, 'prenda_id': prenda_id})

# Vista para eliminar una prenda existente
def eliminar_prenda(request, prenda_id):
    """
    Solicita confirmación para eliminar una prenda.
    Si se confirma por POST, elimina la prenda y redirige a la lista.
    """
    prenda = get_object_or_404(Prenda, id=prenda_id)
    if request.method == 'POST':
        prenda.delete()
        return redirect('buscar_prenda')
    return render(request, 'eliminar_prenda.html', {'prenda': prenda})
