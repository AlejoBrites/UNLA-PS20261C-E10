from django.db import models
from django.conf import settings
from apps.games.models import Game


class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'carrito'
        verbose_name_plural = 'carritos'

    def get_total(self):
        return sum(item.game.price for item in self.items.all())

    def __str__(self):
        return f'Carrito de {self.user.username}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('cart', 'game')
        verbose_name = 'ítem del carrito'
        verbose_name_plural = 'ítems del carrito'

    def __str__(self):
        return f'{self.game.title} — {self.cart.user.username}'
