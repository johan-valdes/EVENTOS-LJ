from django.shortcuts import render, redirect
from .forms import PrendaForm
from .models import Prenda

def registrar_prenda(request):
    if request.method=='POST':
        form = PrendaForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('registro_exitoso')
    else: 
        form = PrendaForm()
    return render(request, 'almacen/registrar_prenda.html', {'form': form})

def registro_exitoso(request): 
    return render (request, 'almacen/registro_exitoso.html')


def lista_prendas(request):
    prendas = Prenda.objects.all()
    return render(request, 'almacen/lista_prendas.html', {'prendas': prendas})

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Prenda

@csrf_exempt
def crear_prenda(request):
    if request.method == "POST":
        data = json.loads(request.body)
        prenda = Prenda.objects.create(
            nombre=data["nombre"],
            talla=data["talla"],
            precio=data["precio"]
        )
        return JsonResponse({
            "id": prenda.id,
            "nombre": prenda.nombre,
            "talla": prenda.talla,
            "precio": str(prenda.precio)
        }, status=201)

@csrf_exempt
def obtener_prenda(request, id):
    try:
        prenda = Prenda.objects.get(pk=id)
        return JsonResponse({
            "id": prenda.id,
            "nombre": prenda.nombre,
            "talla": prenda.talla,
            "precio": str(prenda.precio)
        })
    except Prenda.DoesNotExist:
        return JsonResponse({"error": "No encontrada"}, status=404)

@csrf_exempt
def actualizar_prenda(request, id):
    if request.method == "PUT":
        try:
            prenda = Prenda.objects.get(pk=id)
            data = json.loads(request.body)
            prenda.nombre = data["nombre"]
            prenda.talla = data["talla"]
            prenda.precio = data["precio"]
            prenda.save()
            return JsonResponse({"mensaje": "Actualizado"})
        except Prenda.DoesNotExist:
            return JsonResponse({"error": "No encontrada"}, status=404)

@csrf_exempt
def eliminar_prenda(request, id):
    if request.method == "DELETE":
        try:
            prenda = Prenda.objects.get(pk=id)
            prenda.delete()
            return JsonResponse({"mensaje": "Eliminado"})
        except Prenda.DoesNotExist:
            return JsonResponse({"error": "No encontrada"}, status=404)

def formulario(request):
    return render(request, 'almacen/formulario.html')

from django.shortcuts import render

def formulario(request):
    return render(request, 'almacen/formulario.html')
