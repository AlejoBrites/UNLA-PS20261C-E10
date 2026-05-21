from django.db import models
from django.conf import settings
from apps.games.models import Game


class LibraryEntry(models.Model):
    STATUS_NOT_INSTALLED = 'not_installed'
    STATUS_DOWNLOADING = 'downloading'
    STATUS_INSTALLED = 'installed'
    STATUS_NEEDS_UPDATE = 'needs_update'
    STATUS_CHOICES = [
        (STATUS_NOT_INSTALLED, 'No instalado'),
        (STATUS_DOWNLOADING, 'Descargando'),
        (STATUS_INSTALLED, 'Instalado'),
        (STATUS_NEEDS_UPDATE, 'Necesita actualización'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='library_entries',
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    status = models.CharField('estado', max_length=20, choices=STATUS_CHOICES, default=STATUS_NOT_INSTALLED)
    acquired_at = models.DateTimeField('adquirido el', auto_now_add=True)

    class Meta:
        unique_together = ('user', 'game')
        verbose_name = 'entrada de biblioteca'
        verbose_name_plural = 'entradas de biblioteca'
        ordering = ['-acquired_at']

    def __str__(self):
        return f'{self.game.title} ({self.user.username}) — {self.get_status_display()}'
