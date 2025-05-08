from django.db import models

class Prenda(models.Model):
    tipo_prenda = [('camisa', 'Camisa'),
                   ('pantalon', 'Pantalon'),
                   ('falda', 'Falda'),
                   ('saco', 'Saco'),
                   ('zapatos', 'Zapatos'),
                   ('otro', 'Otro'),
                   ]
    tipo = models.CharField(max_length=20, choices=tipo_prenda)
    marca = models.CharField(max_length=50)
    talla = models.CharField(max_length=10)
    color = models.CharField(max_length=30)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return f"{self.tipo} {self.marca} - {self.color} (talla{self.talla}) "