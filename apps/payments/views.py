from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from apps.cart.models import Cart
from .models import Order, OrderItem, Payment
from apps.library.models import LibraryEntry


@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.select_related('game').all()
    
    # Redirigir si intentan entrar al checkout sin productos
    if not items:
        messages.warning(request, "Tu carrito está vacío.")
        return redirect('games:catalog')
        
    total = cart.get_total()
    balance = request.user.balance
    
    # Validaciones para US14
    insufficient_balance = balance < total
    difference = total - balance if insufficient_balance else 0
    
    context = {
        'cart': cart,
        'items': items,
        'total': total,
        'balance': balance,
        'insufficient_balance': insufficient_balance,
        'difference': difference,
    }
    return render(request, 'payments/checkout.html', context)


@login_required
def confirm_payment(request):
    if request.method != 'POST':
        return redirect('payments:checkout')
        
    cart = get_object_or_404(Cart, user=request.user)
    items = cart.items.select_related('game').all()
    
    if not items:
        messages.warning(request, "Tu carrito está vacío.")
        return redirect('games:catalog')
        
    total = cart.get_total()
    user = request.user
    
    # Doble validación en el servidor por seguridad (US15)
    if user.balance < total:
        messages.error(request, "No tenés saldo suficiente para completar la compra.")
        return redirect('payments:checkout')
        
    try:
        # Bloque atómico: todo o nada
        with transaction.atomic():
            # 1. Descontar el saldo del usuario
            user.balance -= total
            user.save()
            
            # 2. Crear la Orden como Aprobada
            order = Order.objects.create(
                user=user,
                status=Order.STATUS_APPROVED,
                total=total
            )
            
            # 3. Registrar los ítems y agregarlos a la biblioteca activa
            for item in items:
                OrderItem.objects.create(
                    order=order,
                    game=item.game,
                    price=item.game.price
                )
                
                # Agregamos el juego a la biblioteca de juegos adquiridos
                LibraryEntry.objects.get_or_create(
                    user=user,
                    game=item.game,
                    defaults={'status': LibraryEntry.STATUS_NOT_INSTALLED}
                )
            
            # 4. Registrar el comprobante de Pago
            Payment.objects.create(
                order=order,
                method=Payment.METHOD_BALANCE,
                status=Payment.STATUS_APPROVED
            )
            
            # 5. Vaciar completamente el carrito de compras
            cart.items.all().delete()
            
        messages.success(request, "¡Compra realizada con éxito! Los juegos ya están disponibles en tu biblioteca.")
        return redirect('library:library')
        
    except Exception as e:
        messages.error(request, f"Hubo un problema al procesar el pago obligatorio: {str(e)}")
        return redirect('cart:view')
