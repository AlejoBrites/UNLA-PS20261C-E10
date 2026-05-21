# TODO Fase 2 — Integrante 2: Catálogo de juegos
# Branch: feature/games-catalog
# Ver criterios de aceptación en el issue #2.
from django.http import HttpResponse


def catalog(request):
    return HttpResponse("TODO Fase 2: implementar catálogo de juegos.")


def detail(request, slug):
    return HttpResponse(f"TODO Fase 2: implementar detalle del juego '{slug}'.")
