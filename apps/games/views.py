# Fase 1 (parcial): grilla básica de juegos sin búsqueda ni filtros.
# TODO Fase 2 — Integrante 2: agregar búsqueda, filtros por categoría y vista de detalle.
# Branch: feature/games-catalog | Ver criterios en el issue #2.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Game


def catalog(request):
    games = Game.objects.filter(is_available=True).select_related('category')
    return render(request, 'games/catalog.html', {'games': games})


def detail(request, slug):
    # TODO Fase 2 — Integrante 2: implementar detalle del juego
    return HttpResponse(f"TODO Fase 2: implementar detalle del juego '{slug}'.")
