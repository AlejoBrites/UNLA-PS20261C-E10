# TODO Fase 2 — Integrante 2: registrar Category y Game en el admin
from django.contrib import admin
from .models import Category, Game

# Agregamos categoria en el panel admin
admin.site.register(Category)

# Agregamos juegos en el panel de admin
admin.site.register(Game)
