from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar_prenda, name='registrar_prenda'), 
    path('Exito/', views.registro_exitoso, name='registro_exitoso'),
    path('prendas/', views.lista_prendas, name='lista_prendas'),

]

from django.urls import path
from . import views

urlpatterns = [
    path('prendas/', views.crear_prenda),
    path('prendas/<int:id>/', views.obtener_prenda),
    path('prendas/<int:id>/actualizar/', views.actualizar_prenda),
    path('prendas/<int:id>/eliminar/', views.eliminar_prenda),
]

path('formulario/', views.formulario),
