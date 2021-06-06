from django.conf import settings
from django.conf.urls import (
    include, url, handler400, handler403, handler404, handler500
)
from django.conf.urls.static import static
from django.contrib import admin


handler400 = 'shop.views.error_bad_request'
handler403 = 'shop.views.error_permission_denied'
handler404 = 'shop.views.error_page_not_found'
handler500 = 'shop.views.error_server_error'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^coupons/', include('coupons.urls', namespace='coupons')),
    url(r'^', include('shop.urls', namespace='shop')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
