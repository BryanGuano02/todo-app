from django.shortcuts import render, redirect, get_object_or_404
from .models.Tarea import Tarea
from .forms import TareaForm

def tarea_list(request):
    tareas = Tarea.objects.all().order_by('-id')
    return render(request, 'todos/list.html', {'tareas': tareas})

def tarea_create(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarea_list')
    else:
        form = TareaForm()
    return render(request, 'todos/create.html', {'form': form})

def tarea_update(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('tarea_list')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'todos/update.html', {'form': form})

def tarea_delete(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.delete()
    return redirect('tarea_list')
