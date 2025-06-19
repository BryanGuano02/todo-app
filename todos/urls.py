from django.urls import path
from todos import views

urlpatterns = [
    path('', views.tarea_list, name='tarea_list'),
    path('crear/', views.tarea_create, name='tarea_create'),
    path('actualizar/<int:pk>/', views.tarea_update, name='tarea_update'),
    path('eliminar/<int:pk>/', views.tarea_delete, name='tarea_delete'),
]
