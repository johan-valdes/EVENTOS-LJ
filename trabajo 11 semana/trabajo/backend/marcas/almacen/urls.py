from django.urls import path
from . import views
from django.http import HttpResponse  # Import necesario

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registrar/', views.registrar_prenda, name='registrar_prenda'),
    path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),
    path('lista/', views.lista_prendas, name='lista_prendas'),
    path('buscar/', views.buscar_prenda, name='buscar_prenda'),
    path('actualizar/<int:prenda_id>/', views.actualizar_prenda, name='actualizar_prenda'),
    path('eliminar/<int:prenda_id>/', views.eliminar_prenda, name='eliminar_prenda'),

    # 🚫 Ignorar favicon.ico con una respuesta vacía (204 No Content)
    path('favicon.ico', lambda request: HttpResponse(status=204)),
]

