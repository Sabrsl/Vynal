# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Utilitaire en ligne de commande de Django pour les t�ches administratives.
import os
import sys


def main():
    """Ex�cuter les t�ches administratives."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vynal_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Impossible d'importer Django. �tes-vous s�r qu'il est install� et "
            "disponible dans votre variable d'environnement PYTHONPATH ? Avez-vous "
            "oubli� d'activer un environnement virtuel ?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
