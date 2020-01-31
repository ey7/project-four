from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def cart_view(request):

	return render(request, 'cart/cart_view.html')

# function to increment cart items on cart page
@login_required
def add_to_cart(request, id):
	# increments product count of 1 product name in the cart
	
	if request.method == 'POST':
		id = request.POST.get('id')
		cart = request.session.get('cart', {})
		cart[id] = cart.get(id, 0) + 1
		request.session['cart'] = cart

		return render(request,'cart/cart_view.html')
		
# function to add product to cart on products and search pages
@login_required
def add_product_to_cart(request, id):
	# adds selected product to the cart
	
	if request.method == 'GET':
		return redirect(reverse('login'))

		if request.method == 'POST':
			id = request.POST.get('id')
			cart = request.session.get('cart', {})
			cart[id] = cart.get(id, 0) + 1
			request.session['cart'] = cart
			messages.info(request, f'Product added to cart')

			return redirect(reverse('products:all-products'))

# function to decrement cart items on cart page
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




