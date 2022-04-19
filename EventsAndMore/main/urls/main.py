from django.urls import path
from django.views.generic import TemplateView

from main.views import services_view
from main.views.accounts import RegisterClientView
from main.views.cart import remove_cart_element, show_cart_view, update_producto_view
from main.views.incidences import NuevaIncidencia, Incidencias

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('register/client', RegisterClientView, name='register_client'),
    path('servicios/<int:evento>', services_view, name='evento_servicios'),
    path('cart/', show_cart_view, name='cart'),
    path('cart/remove/<int:id_producto>', remove_cart_element, name='remove_cart_element'),
    path('cart/update/', update_producto_view, name='update_product'),
    path('incidencies/', Incidencias, name='incidencias'),
    path('incidencies/nueva', NuevaIncidencia, name='nueva_incidencia'),
]
