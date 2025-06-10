from django.urls import path
from . import views

urlpatterns = [
    path('autores/', views.crear_autor),
    path('autores/listar/', views.listar_autores),
    path('libros/', views.crear_libro),
    path('libros/listar/', views.listar_libros),
]
