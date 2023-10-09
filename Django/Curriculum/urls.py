from django.urls import path
from . import views

urlpatterns = [
    path("Practica2/", views.PrimerPagina, name = "PrimeraPagina")
]