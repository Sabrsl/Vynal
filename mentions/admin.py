# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Mention, Utilisateur


@admin.register(Mention)
class MentionAdmin(admin.ModelAdmin):
    list_display = (
        "contenu",
        "date_creation",
        "utilisateur",
        "source",
        "sentiment")
    search_fields = (
        "contenu",
        "source",
        "utilisateur__prenom",
        "utilisateur__nom")
    list_filter = ("sentiment", "date_creation")


@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ("prenom", "nom", "email", "numero_telephone")
    search_fields = ("prenom", "nom", "email")
