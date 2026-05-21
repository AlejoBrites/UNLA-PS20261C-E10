from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/confirm/', views.confirm_payment, name='confirm'),
]
