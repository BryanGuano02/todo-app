from django.utils import timezone


class Tarea_Service:
    @staticmethod
    def toggle_estado(tarea):
        if tarea.fecha_limite and tarea.fecha_limite < timezone.now():
            raise ValueError("No se puede completar una tarea vencida.")
        tarea.completada = not tarea.completada
        return tarea
