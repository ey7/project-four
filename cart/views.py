from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

@login_required
def cart_view(request):

	return render(request, 'cart/cart_view.html')

@login_required
def add_to_cart(request, id):
	# adds one product to the cart
	
	if request.method == 'POST':
		id = request.POST.get('id')
		cart = request.session.get('cart', {})
		cart[id] = cart.get(id, 0) + 1
		request.session['cart'] = cart

		return render(request,'cart/cart_view.html')

@login_required
def remove_from_cart(request, id):
	# remove only one item from the cart, if empty, delete

	if request.method == 'POST':
		id = request.POST.get('id')
		cart = request.session.get('cart', {})

		if id in cart:
			cart[id] -= 1
			if cart[id] == 0:
			 	del cart[id]
			request.session['cart'] = cart

			return render(request, 'cart/cart_view.html')

@login_required
def remove_all_of_one_item_from_cart(request, id):
	# remove all of one particular item from cart
	if request.method == 'POST':
		id = request.POST.get('id')
		cart = request.session.get('cart', {})

		if id in cart and cart[id] > 0:
			del cart[id]
			
			request.session['cart'] = cart

		return render(request, 'cart/cart_view.html')




