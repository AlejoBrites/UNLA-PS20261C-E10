from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, CartItem
from apps.games.models import Game


@login_required
def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart.html', {'cart': cart})


@login_required
def add_to_cart(request, game_id):
    game = get_object_or_404(Game, id=game_id, is_available=True)

    # Evitar agregar un juego que ya está en la biblioteca
    if request.user.library_entries.filter(game=game).exists():
        messages.info(request, f'Ya tenés "{game.title}" en tu biblioteca.')
        return redirect('games:detail', slug=game.slug)

    cart, _ = Cart.objects.get_or_create(user=request.user)
    _, created = CartItem.objects.get_or_create(cart=cart, game=game)

    if created:
        messages.success(request, f'"{game.title}" agregado al carrito.')
    else:
        messages.info(request, f'"{game.title}" ya estaba en el carrito.')

    return redirect('games:catalog')


@login_required
def remove_from_cart(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    cart = get_object_or_404(Cart, user=request.user)
    deleted, _ = CartItem.objects.filter(cart=cart, game=game).delete()
    if deleted:
        messages.success(request, f'"{game.title}" eliminado del carrito.')
    return redirect('cart:view')
