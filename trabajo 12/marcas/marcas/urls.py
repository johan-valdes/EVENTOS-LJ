from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('almacen.urls')),  
]

from django.urls import path
from . import views

urlpatterns = [
    path('prendas/', views.crear_prenda),
    path('prendas/<int:id>/', views.obtener_prenda),
    path('prendas/<int:id>/actualizar/', views.actualizar_prenda),
    path('prendas/<int:id>/eliminar/', views.eliminar_prenda),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('almacen.urls')),
]
