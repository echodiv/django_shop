from django.conf.urls import url
from django.views.generic import TemplateView

from .views import CartView


app_name = 'cart'


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='cart/details.html'),
        name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', CartView.as_view(), name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', CartView.as_view(),
        name='cart_remove'),
]
