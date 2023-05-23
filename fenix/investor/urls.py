from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.myinvestments, name='investments'),
    path('addBalance', views.addBalance, name='addBalance'),
    path('paypalMethod', views.paypalPaymethod, name='paypalPaymethod'),
    path('paypal-cancel', views.paypal_cancel, name='paypal-cancel'),
    path('paypal-return', views.paypal_return, name='paypal-return'),
    path('paypal/', include("paypal.standard.ipn.urls")),
]