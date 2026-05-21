from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .models import Order, OrderItem, Payment
from apps.cart.models import Cart
from apps.library.models import LibraryEntry


@login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user).first()
    if not cart or not cart.items.exists():
        messages.warning(request, 'Tu carrito está vacío.')
        return redirect('cart:view')

    total = cart.get_total()
    return render(request, 'payments/checkout.html', {
        'cart': cart,
        'total': total,
        'balance': request.user.balance,
        'has_enough_balance': request.user.balance >= total,
    })


@login_required
@transaction.atomic
def confirm_payment(request):
    if request.method != 'POST':
        return redirect('payments:checkout')

    cart = Cart.objects.filter(user=request.user).first()
    if not cart or not cart.items.exists():
        return redirect('cart:view')

    total = cart.get_total()
    user = request.user

    order = Order.objects.create(user=user, total=total, status=Order.STATUS_PENDING)
    for item in cart.items.select_related('game').all():
        OrderItem.objects.create(order=order, game=item.game, price=item.game.price)

    if user.balance >= total:
        user.balance -= total
        user.save(update_fields=['balance'])
        order.status = Order.STATUS_APPROVED
        order.save(update_fields=['status'])
        Payment.objects.create(order=order, method=Payment.METHOD_BALANCE, status=Payment.STATUS_APPROVED)

        for item in cart.items.select_related('game').all():
            LibraryEntry.objects.get_or_create(user=user, game=item.game)

        cart.items.all().delete()
        messages.success(request, '¡Compra realizada con éxito! Los juegos ya están en tu biblioteca.')
        return redirect('library:library')
    else:
        order.status = Order.STATUS_REJECTED
        order.save(update_fields=['status'])
        Payment.objects.create(order=order, method=Payment.METHOD_BALANCE, status=Payment.STATUS_REJECTED)
        messages.error(request, f'Saldo insuficiente. Necesitás ${total} pero tenés ${user.balance}.')
        return redirect('payments:checkout')
