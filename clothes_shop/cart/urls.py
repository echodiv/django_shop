from django.conf.urls import url
from django.views.generic import TemplateView

from .views import CartManagerView, CartView


app_name = 'cart'


urlpatterns = [
    url(r'^$', CartView.as_view(), name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', CartManagerView.as_view(),
        name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', CartManagerView.as_view(),
        name='cart_remove'),
]
