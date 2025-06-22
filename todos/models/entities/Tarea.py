from django.db import models

# Create your models here.
class Tarea(models.Model):
    CATEGORIAS = [
        ('Universidad', 'Universidad'),
        ('Personal', 'Personal'),
        ('Trabajo', 'Trabajo'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100, choices=CATEGORIAS, default='Personal')
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateTimeField(null=True, blank=True)
    recordatorio = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.titulo
