from django.urls import path
from . import views

urlpatterns = [
	path('', views.cart_view, name="cart"),
	path('add-to-cart/<int:id>/', views.add_to_cart, name="add-to-cart"),
	path('add-product-to-cart/<int:id>/', views.add_product_to_cart, name="add-product-to-cart"),
	path('remove-from-cart/<int:id>/', views.remove_from_cart, name="remove-from-cart"),
	path('remove-all-from-cart/<int:id>/', views.remove_all_of_one_item_from_cart,
		name="remove-all-from-cart"),
]

