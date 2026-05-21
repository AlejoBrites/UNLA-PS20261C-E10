# TODO Fase 3 — Integrante 3: Carrito de compras
# Branch: feature/cart-management
# Ver criterios de aceptación en el issue #2.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def view_cart(request):
    return HttpResponse("TODO Fase 3: implementar vista del carrito.")


@login_required
def add_to_cart(request, game_id):
    return HttpResponse("TODO Fase 3: implementar agregar al carrito.")


@login_required
def remove_from_cart(request, game_id):
    return HttpResponse("TODO Fase 3: implementar eliminar del carrito.")
