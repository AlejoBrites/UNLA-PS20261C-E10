from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='view'),
    path('add/<int:game_id>/', views.add_to_cart, name='add'),
    path('remove/<int:game_id>/', views.remove_from_cart, name='remove'),
]
