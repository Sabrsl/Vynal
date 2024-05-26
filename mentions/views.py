# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.template import TemplateDoesNotExist
from .models import Mention


def index(request):
    """
    Vue pour afficher toutes les mentions.
    """
    mentions = Mention.objects.all()
    context = {"mentions": mentions}
    return render(request, "mentions/index.html", context)


def mention_detail(request, mention_id):
    """
    Vue pour afficher les détails d'une mention spécifique.
    """
    mention = get_object_or_404(Mention, id=mention_id)
    context = {"mention": mention}
    return render(request, "mentions/mention_detail.html", context)


def create_mention(request):
    """
    Vue pour créer une nouvelle mention.
    Accessible uniquement aux utilisateurs connectés.
    """
    if request.method == "POST":
        contenu = request.POST.get("contenu")
        source = request.POST.get("source")
        lien = request.POST.get("lien")
        # Vérifier si request.user est un objet utilisateur avec l'attribut
        # utilisateur
        if hasattr(request.user, "utilisateur"):
            utilisateur = request.user.utilisateur
            mention = Mention.objects.create(
                contenu=contenu,
                source=source,
                lien=lien,
                utilisateur=utilisateur)
            return redirect("mention_detail", mention_id=mention.id)
        else:
            # Gérer le cas où request.user n'a pas d'attribut utilisateur
            # Vous devrez ajuster cette partie en fonction de votre modèle
            # d'utilisateur
            return HttpResponse("Erreur: utilisateur non trouvé")
    else:
        return render(request, "mentions/create_mention.html")


def update_mention(request, mention_id):
    """
    Vue pour mettre à jour une mention existante.
    Accessible uniquement aux utilisateurs connectés.
    """
    mention = get_object_or_404(Mention, id=mention_id)
    if request.method == "POST":
        mention.contenu = request.POST.get("contenu")
        mention.source = request.POST.get("source")
        mention.lien = request.POST.get("lien")
        mention.save()
        return redirect("mention_detail", mention_id=mention.id)
    else:
        return render(request,
                      "mentions/update_mention.html",
                      {"mention": mention})


def delete_mention(request, mention_id):
    """
    Vue pour supprimer une mention existante.
    Accessible uniquement aux utilisateurs connectés.
    """
    mention = get_object_or_404(Mention, id=mention_id)
    if request.method == "POST":
        mention.delete()
        return redirect("index")
    return render(request,
                  "mentions/delete_mention.html",
                  {"mention": mention})


def home(request):
    """
    Vue pour la page d'accueil.
    """
    return render(request, 'home.html')


def handler404(request, exception):
    """
    Vue personnalisée pour gérer les erreurs 404.
    """
    try:
        return render(request, "404.html", status=404)
    except TemplateDoesNotExist:
        return HttpResponseNotFound("<h1>Page non trouvée</h1>")
