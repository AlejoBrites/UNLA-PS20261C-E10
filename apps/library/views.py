# TODO Fase 5 — Integrante 5: Biblioteca personal
# Branch: feature/library-download
# Ver criterios de aceptación en el issue #2.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.library.models import LibraryEntry
 
 
@login_required
def library(request):
    # Obtenemos todos los juegos comprados por el usuario a través de la biblioteca
    library_entries = LibraryEntry.objects.filter(
        user=request.user
    ).select_related('game', 'game__category')
 
    games = [entry.game for entry in library_entries]
 
    return render(request, 'library/library.html', {'games': games})