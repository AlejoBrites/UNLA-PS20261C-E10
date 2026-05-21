from django.db import models
from django.conf import settings
from apps.games.models import Game


class Order(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pendiente'),
        (STATUS_APPROVED, 'Aprobado'),
        (STATUS_REJECTED, 'Rechazado'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
    )
    status = models.CharField('estado', max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    total = models.DecimalField('total', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'orden'
        verbose_name_plural = 'órdenes'
        ordering = ['-created_at']

    def __str__(self):
        return f'Orden #{self.pk} — {self.user.username} ({self.get_status_display()})'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    # SET_NULL para conservar el historial si el juego es eliminado
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField('precio al momento de la compra', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'ítem de orden'
        verbose_name_plural = 'ítems de orden'

    def __str__(self):
        return f'{self.game} — Orden #{self.order.pk}'


class Payment(models.Model):
    METHOD_BALANCE = 'balance'
    METHOD_CHOICES = [
        (METHOD_BALANCE, 'Saldo en cuenta'),
    ]
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'
    STATUS_CHOICES = [
        (STATUS_APPROVED, 'Aprobado'),
        (STATUS_REJECTED, 'Rechazado'),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    method = models.CharField('método de pago', max_length=20, choices=METHOD_CHOICES, default=METHOD_BALANCE)
    status = models.CharField('estado', max_length=20, choices=STATUS_CHOICES)
    processed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'pago'
        verbose_name_plural = 'pagos'

    def __str__(self):
        return f'Pago orden #{self.order.pk} — {self.get_status_display()}'
