from django.urls import path
from . views import checkout, checkout_confirm

urlpatterns = [
	path('', checkout, name="checkout"),
	path('confirm/', checkout_confirm, name="checkout_confirm")
]