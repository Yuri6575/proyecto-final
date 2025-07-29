from django.urls import path
from . import views


#vistas basadas en funciones
urlpatterns = [
    path('', views.lista_citas, name='lista_citas'),
    path('nueva/', views.crear_cita, name='crear_cita'),
    path('editar/<int:pk>/', views.editar_cita, name='editar_cita'),
    path('eliminar/<int:pk>/', views.eliminar_cita, name='eliminar_cita'),
]