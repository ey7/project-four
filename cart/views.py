from django.shortcuts import render, redirect, reverse
from . models import OrderLineItem
from products.models import Product

def cart_view(request):
	cart_items = OrderLineItem.objects.filter(customer=request.user)

	return render(request, 'cart/cart_view.html',{
		'cart_items':cart_items
		} ) 

def add_to_cart(request, id):
	# assign product variable
	product = Product.objects.get(id=id)
	# determine if the product already exists in users cart
	existing_item_in_cart = OrderLineItem.objects.filter(customer=request.user, product=product).first()
	# if item is not there, create a new one
	if existing_item_in_cart == None:
		new_item_in_cart = OrderLineItem()
		new_item_in_cart.product = product
		new_item_in_cart.customer = request.user
		new_item_in_cart.quantity = 1
		new_item_in_cart.save()
	else:
		# increase total in cart
		existing_item_in_cart += 1
		existing_item_in_cart.save()

		return render(request, 'cart/cart_view.html')



