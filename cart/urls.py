from django.urls import path
from . import views

urlpatterns = [
	path('', views.cart_view, name="cart"),
	path('add-to-cart/<int:id>/', views.add_to_cart, name="add-to-cart"),
	path('remove-from-cart/<int:id>/', views.remove_from_cart, name="remove-from-cart"),
]

