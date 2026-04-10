from django.db import models

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

    def __str__(self):
        return f"{self.nombre} (${self.precio})"