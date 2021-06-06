from django.conf.urls import url

from .views import CouponApplyView

app_name = 'coupons'

urlpatterns = [
    url(r'^apply/$', CouponApplyView.as_view(), name='apply')
]
