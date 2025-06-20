from django import forms
from .models.entities.Tarea import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'categoria', 'completada', 'fecha_limite']
