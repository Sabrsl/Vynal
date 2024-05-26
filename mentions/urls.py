# C:\Users\sabrs\Desktop\Vynal\vynal-web\vynal_backend\mentions\urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Page d'accueil accessible sans connexion
    path("", views.home, name="home"),
    path("mentions/", views.index, name="index"),
    path(
        "mention/<int:mention_id>/",
        views.mention_detail,
        name="mention_detail"),
    path("mention/create/", views.create_mention, name="create_mention"),
    path(
        "mention/update/<int:mention_id>/",
        views.update_mention,
        name="update_mention"),
    path(
        "mention/delete/<int:mention_id>/",
        views.delete_mention,
        name="delete_mention"),
]
