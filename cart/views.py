from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

@login_required
def cart_view(request):

	return render(request, 'cart/cart_view.html')

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
		return render(request,'cart/cart_view.html')

@login_required
def remove_from_cart(request, id):
	# remove an item from the cart

	if request.method == 'POST':
		item_remove = request.POST.get('id')
		cart = request.session.get('cart', {})

		if cart[item_remove] > 0:
			cart.pop(item_remove)
			request.session['cart'] = cart

			return redirect(reverse('cart'))

