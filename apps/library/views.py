# TODO Fase 5 — Integrante 5: Biblioteca personal
# Branch: feature/library-download
# Ver criterios de aceptación en el issue #2.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def library(request):
    return HttpResponse("TODO Fase 5: implementar biblioteca personal.")


@login_required
def update_status(request, entry_id):
    return HttpResponse("TODO Fase 5: implementar actualización de estado.")
