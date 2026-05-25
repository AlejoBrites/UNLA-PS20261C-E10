# TODO Fase 3 — Integrante 3: registrar Cart y CartItem en el admin
from django.contrib import admin
from .models import Cart, CartItem

#Agrego en el panel de admin el carrito
admin.site.register(Cart)

#Agrego en el panel de admin el item del carrito
admin.site.register(CartItem)