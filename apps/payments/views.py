# TODO Fase 4 — Integrante 4: Checkout y pagos simulados
# Branch: feature/payments-checkout
# Ver criterios de aceptación en el issue #2.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def checkout(request):
    return HttpResponse("TODO Fase 4: implementar checkout.")


@login_required
def confirm_payment(request):
    return HttpResponse("TODO Fase 4: implementar confirmación de pago.")
