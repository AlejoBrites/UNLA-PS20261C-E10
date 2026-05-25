# TODO Fase 5 — Integrante 5: Biblioteca personal
# Branch: feature/library-download
# Ver criterios de aceptación en el issue #2.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.cart.models import CartItem
 
 
@login_required
def library(request):
    # Obtenemos todos los juegos comprados por el usuario a través del carrito
    purchased_items = CartItem.objects.filter(
        cart__user=request.user
    ).select_related('game', 'game__category')
 
    games = [item.game for item in purchased_items]
 
    return render(request, 'library/library.html', {'games': games})