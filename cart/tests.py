from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

class TestCartPages(TestCase):

	def test_cartview_template(self):
	# will check to see if cart view gives 302 redirect as the user must be logged in
		response = self.client.get('/cart/')
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/carts/')
		# check to see if the url carts will produce a 404
		self.assertEqual(response.status_code, 404)
		self.assertTemplateNotUsed(response, 'cart/cart.html')




	
		


