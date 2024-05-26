# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class Utilisateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    numero_telephone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class VynalBackend(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    createur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    categorie = models.CharField(max_length=100, blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    visibilite = models.CharField(
        max_length=20,
        choices=[("public", "Public"), ("prive", "Prive")],
        default="public",
    )
    statut = models.CharField(
        max_length=20,
        choices=[
            ("brouillon", "Brouillon"),
            ("publie", "Publie"),
            ("archive", "Archive"),
        ],
        default="brouillon",
    )

    def __str__(self):
        return self.titre


class Commentaire(models.Model):
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    vynal_backend = models.ForeignKey(
        VynalBackend, on_delete=models.CASCADE, related_name="commentaires"
    )

    def __str__(self):
        return f"Commentaire de {self.auteur} sur {self.vynal_backend}"


class Tag(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom


class VynalSentiment(models.Model):
    vynal_backend = models.OneToOneField(
        VynalBackend, on_delete=models.CASCADE, related_name="sentiment"
    )
    sentiment = models.CharField(
        max_length=10, choices=[
            ("positif", "Positif"), ("negatif", "Negatif"), ("neutre", "Neutre")], )
    score = models.FloatField()

    @classmethod
    def create(cls, vynal_backend):
        analyzer = SentimentIntensityAnalyzer()
        sentiment_score = analyzer.polarity_scores(
            vynal_backend.titre + " " + vynal_backend.description
        )

        if sentiment_score["compound"] >= 0.05:
            sentiment = "positif"
        elif sentiment_score["compound"] <= -0.05:
            sentiment = "negatif"
        else:
            sentiment = "neutre"

        return cls(
            vynal_backend=vynal_backend,
            sentiment=sentiment,
            score=sentiment_score["compound"],
        )

    def __str__(self):
        return f"Sentiment de {self.vynal_backend}: {self.sentiment}"
