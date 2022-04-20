from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from main.cart import Cart
from main.decorators import event_is_validated, cliente_only
from main.models import Cliente


@cliente_only
@event_is_validated
def show_cart_view(request, **kwargs):
    id_evento = kwargs.get('evento')
    id_stand = kwargs.get('stand')
    cliente = Cliente.objects.get(user=request.user)

    cart = Cart(evento=id_evento, stand=id_stand, cliente=cliente)

    return render(request, 'services/cart.html', {'cart': cart})


@login_required
def remove_cart_element(request):
    if request.POST:
        try:
            id_evento = request.POST.get('id_evento')
            id_stand = request.POST.get('id_stand')
            id_servicio = request.POST.get('id_servicio')
            cliente = Cliente.objects.get(user=request.user)
            cart = Cart(cliente=cliente, evento=id_evento, stand=id_stand)
            cart.remove(id_servicio)

            return HttpResponseRedirect(reverse('cart', kwargs={'evento': id_evento, 'stand': id_stand}))
        except KeyError:
            return HttpResponseRedirect(reverse('cart'))

    return HttpResponseRedirect(reverse('cart'))


@login_required
def update_producto_view(request):
    if request.POST:
        try:
            id_evento = request.POST.get('id_evento')
            id_stand = request.POST.get('id_stand')
            id_servicio = request.POST.get('id_servicio')
            quantity = int(request.POST['quantity'])

            cliente = Cliente.objects.get(user=request.user)

            cart = Cart(cliente=cliente, evento=id_evento, stand=id_stand)
            cart.set_quantity(id_servicio, quantity)

            return JsonResponse({'status': 'ok', 'total': cart.total})
        except KeyError:
            return HttpResponseRedirect(reverse('cart'))

    return HttpResponseRedirect(reverse('cart'))
