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


class Mention(models.Model):
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    lien = models.URLField(max_length=200)
    SENTIMENT_CHOICES = [
        ('positif', 'Positif'),
        ('negatif', 'Négatif'),
        ('neutre', 'Neutre'),
    ]
    sentiment = models.CharField(
        max_length=10,
        choices=SENTIMENT_CHOICES
    )

    def save(self, *args, **kwargs):
        analyzer = SentimentIntensityAnalyzer()
        sentiment_score = analyzer.polarity_scores(self.contenu)
        if sentiment_score['compound'] >= 0.05:
            self.sentiment = 'positif'
        elif sentiment_score['compound'] <= -0.05:
            self.sentiment = 'negatif'
        else:
            self.sentiment = 'neutre'
        super().save(*args, **kwargs)
