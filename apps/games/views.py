# Fase 1 (parcial): grilla básica de juegos sin búsqueda ni filtros.
# TODO Fase 2 — Integrante 2: agregar búsqueda, filtros por categoría y vista de detalle.
# Branch: feature/games-catalog | Ver criterios en el issue #2.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Game
 
 
def catalog(request):
    games = Game.objects.filter(is_available=True).select_related('category')
    return render(request, 'games/catalog.html', {'games': games})
 
 
def detail(request, slug):
    game = get_object_or_404(Game, slug=slug, is_available=True)
    return render(request, 'games/detail.html', {'game': game})
 