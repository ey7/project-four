from django.test import TestCase
from django.shortcuts import reverse

class TestCheckoutPages(TestCase):

	def test_cartview_template(self):
		# will check to see if checkout view gives 302 redirect as the user must be logged in
		response = self.client.get('/checkout/')
		self.assertEqual(response.status_code, 302)
		self.client.post(reverse('checkout'))
