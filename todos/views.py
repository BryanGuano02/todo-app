from django.shortcuts import render, redirect, get_object_or_404
from .models.services.tareas_service import Tarea_Service
from .models.entities.Tarea import Tarea
from .forms import TareaForm

def listar_tareas(request):
    tareas = Tarea.objects.all().order_by('-id')
    return render(request, 'lista.html', {'tareas': tareas})

def crear_tarea(request):
    if request.method == 'POST':
        return manejar_tarea_post(request)

    form = TareaForm()
    return render(request, 'crear.html', {'form': form})

def actualizar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)

    if request.method == 'POST':
        return manejar_tarea_post(request, tarea)

    form = TareaForm(instance=tarea)
    return render(request, 'actualizar.html', {'form': form})

def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.delete()
    return redirect('tarea_list')

def alternar_estado_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea = Tarea_Service.alternar_estado(tarea)
    tarea.save()
    return redirect('tarea_list')

def manejar_tarea_post(request, instance=None):
    form = TareaForm(request.POST, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('tarea_list')

    template = 'actualizar.html' if instance else 'crear.html'
    return render(request, template, {'form': form})
