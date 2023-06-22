from django.urls import path, include
from .views import *

urlpatterns = [
    path("callback/", payment_handler, name="payment_handler"),
    path("payment/success", success_view),
]
