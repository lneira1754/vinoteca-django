from django.db import models

class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre



class Vino(models.Model):
    TIPOS_VINO = [
        ('Cabernet', 'Cabernet'),
        ('Chardonnay', 'Chardonnay'),
        ('Malbec', 'Malbec'),
        ('Merlot', 'Merlot'),
        # Puedes agregar más aquí
    ]

    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=50, choices=TIPOS_VINO)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, related_name='vinos', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} (${self.precio})"
