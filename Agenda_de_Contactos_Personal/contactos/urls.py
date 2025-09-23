from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_contactos, name='lista_contactos'),                    #ruta lista
    path('agregar/', views.agregar_contacto, name='agregar_contacto'),          #ruta agregar
    path('editar/<int:id>/', views.editar_contacto, name='editar_contacto'),    #ruta editar
    path('borrar/<int:id>/', views.borrar_contacto, name='borrar_contacto'),    #ruta borrar
]
