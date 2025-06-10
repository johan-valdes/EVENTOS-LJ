from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Autor, Libro

@csrf_exempt
def crear_autor(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        autor = Autor.objects.create(**data)
        return JsonResponse({'id': autor.id})
    return JsonResponse({'detail': 'Método no permitido'}, status=405)

@csrf_exempt
def listar_autores(request):
    autores = list(Autor.objects.values())
    return JsonResponse(autores, safe=False)

@csrf_exempt
def crear_libro(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        libro = Libro.objects.create(**data)
        return JsonResponse({'id': libro.id})
    return JsonResponse({'detail': 'Método no permitido'}, status=405)

@csrf_exempt
def listar_libros(request):
    libros = list(Libro.objects.values())
    return JsonResponse(libros, safe=False)