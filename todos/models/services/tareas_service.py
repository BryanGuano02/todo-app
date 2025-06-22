from django.utils import timezone


class Tarea_Service:
    @staticmethod
    def alternar_estado(tarea):
        if tarea.fecha_limite and tarea.fecha_limite < timezone.now():
            raise ValueError("No se puede completar una tarea vencida.")
        tarea.completada = not tarea.completada
        return tarea

    def tareas_proximas_a_vencer(request):
        hoy = timezone.now().date()
        proximas = Tarea.objects.filter(completada=False,
                                       fecha_vencimiento__lte=hoy+timedelta(days=3))
        return render(request, 'proximas.html', {'tareas': proximas})
