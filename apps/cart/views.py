# TODO Fase 3 — Integrante 3: Carrito de compras
# Branch: feature/cart-management
# Ver criterios de aceptación en el issue #2.
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, CartItem
from apps.games.models import Game
from apps.library.models import LibraryEntry

@login_required
def view_cart(request):
    # get_or_create asegura que el usuario siempre tenga un carrito vinculado
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # select_related optimiza la consulta a la base de datos trayendo los datos del juego de una vez
    items = cart.items.select_related('game').all()
    
    return render(request, 'cart/cart.html', {'cart': cart, 'items': items})


@login_required
def add_to_cart(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    
    # 1. Validar si ya lo tiene en su biblioteca (Criterio de US11)
    if LibraryEntry.objects.filter(user=request.user, game=game).exists():
        messages.warning(request, f"Ya tenés '{game.title}' en tu biblioteca.")
        return redirect('games:catalog')
        
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # 2. Validar si ya está en el carrito (Criterio de US11)
    if CartItem.objects.filter(cart=cart, game=game).exists():
        messages.info(request, f"'{game.title}' ya está en tu carrito.")
    else:
        # 3. Si pasa las validaciones, lo agregamos
        CartItem.objects.create(cart=cart, game=game)
        messages.success(request, f"'{game.title}' fue agregado al carrito.")
        
    return redirect('cart:view')

@login_required
def remove_from_cart(request, game_id):
    cart = get_object_or_404(Cart, user=request.user)
    game = get_object_or_404(Game, id=game_id)
    
    # Buscamos el ítem específico y lo eliminamos (Criterio de US13)
    item = CartItem.objects.filter(cart=cart, game=game).first()
    if item:
        item.delete()
        messages.success(request, f"'{game.title}' fue eliminado del carrito.")
        
    return redirect('cart:view')
