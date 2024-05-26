# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from mentions import views

urlpatterns = [
    path("admin/", admin.site.urls),  # URL de l'administration Django
    path("", views.index, name="index"),  # URL de la page d'accueil
    path(
        "mentions/", include("mentions.urls")
    ),  # Inclure les URLs de l'application "mentions"
    # Ajoutez d'autres URLs selon les besoins de votre application
]

# Gestion des erreurs 404
handler404 = "mentions.views.handler404"  # Handler pour les erreurs 404
