from django.conf.urls import  url

from .views import OrderView


app_name = 'orders'

urlpatterns = [
    url(r'^create/$', OrderView.as_view(), name='order_create'),
]
