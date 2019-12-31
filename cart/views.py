from django.shortcuts import render, redirect, reverse
from . models import OrderLineItem, Order
from products.models import Product

def cart_view(request):
	cart_items = OrderLineItem.objects.filter()

	return render(request, 'cart/cart_view.html',{
		'cart_items':cart_items
		} ) 

