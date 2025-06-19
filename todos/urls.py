from django.urls import path
from todos import views

urlpatterns = [
    path('', views.tarea_list, name='tarea_list'),
    path('create/', views.tarea_create, name='tarea_create'),
    path('update/<int:pk>/', views.tarea_update, name='tarea_update'),
    path('delete/<int:pk>/', views.tarea_delete, name='tarea_delete'),
]
