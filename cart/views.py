from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

@login_required
def cart_view(request, id , quantity):
	if quantity in cart:
		cart[quantity] = int(cart[quantity])
	else:
		cart[quantity] = cart.get(quantity, id)

	return render(request, 'cart/cart_view.html',{'quantity':quantity,})

@login_required
def add_to_cart(request, id):
	# add a quantity of product to the cart
	quantity = int(request.POST.get('quantity'))

	cart = request.session.get('cart', {})
	if id in cart:
		cart[id] = int(cart[id]) + quantity
	else:
		cart[id] = cart.get(id, quantity)

		request.session['cart'] = cart
		return render(request,'cart/cart_view.html',{'quantity':quantity,})




