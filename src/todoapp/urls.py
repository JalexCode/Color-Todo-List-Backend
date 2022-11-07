from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todoapp.api.views import TaskViewSet

routers = DefaultRouter()
routers.register(r'tasks', TaskViewSet)

urlpatterns = [path("api/", include(routers.urls)),
               # path('api/eliminar/<int:pk>/', views.eliminarTarea, name='eliminarTarea'),
               # path('api/completar/<int:pk>/', views.completarTarea, name='completar'),
               # path('api/insertar/', views.insertarTarea, name='insertarTarea'),
               # path('tareas/eliminarCompletados/', views.eliminarCompletados, name='eliminarCompletados'),
               # path('tareas/completadas/', views.filtrarTareasCompletadas, name='filtrarTareasCompletadas'),
               # path('tareas/noCompletadas/', views.filtrarTareasNoCompletadas, name='filtrarTareasNoCompletadas'),
               # path('tareas/', views.obtenerTareas, name='obtenerTareas'),
               # path('tarea/detalles/<int:pk>/', views.obtenerComentarios, name='obtenerComentarios'),
               # path('tarea/insertarComentario/', views.insertarComentario, name='insertarComentario'),
               ]