from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField('nombre', max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField('título', max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField('descripción')
    price = models.DecimalField('precio', max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        Category,
        verbose_name='categoría',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='games',
    )
    image = models.ImageField('imagen', upload_to='games/', blank=True, null=True)
    developer = models.CharField('desarrollador', max_length=200)
    release_date = models.DateField('fecha de lanzamiento', blank=True, null=True)
    is_available = models.BooleanField('disponible', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'juego'
        verbose_name_plural = 'juegos'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
