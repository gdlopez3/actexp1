"""
    Manejo de urls para la aplicación
"""
from django.urls import path
# se importa las vistas de la aplicación
from financiero import views


urlpatterns = [
        path('', views.bancos, name='bancos'),
 ]
