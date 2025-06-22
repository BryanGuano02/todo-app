from django.urls import path
from todos import views

urlpatterns = [
    path('', views.listar_tareas, name='tarea_list'),
    path('crear/', views.crear_tarea, name='tarea_create'),
    path('actualizar/<int:pk>/', views.actualizar_tarea, name='tarea_update'),
    path('eliminar/<int:pk>/', views.eliminar_tarea, name='tarea_delete'),
    path('toggle-estado/<int:pk>/', views.alternar_estado_tarea, name='tarea_toggle_estado'),
]
