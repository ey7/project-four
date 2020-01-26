from django.test import TestCase
from django.shortcuts import reverse


class TestUserPages(TestCase):

	def test_register(self):
		# will check the register view
		response = self.client.get('/users/register/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'users/register.html')

	def test_account_page(self):
		response = self.client.get('/users/account/')
		# check that the page will redirect to account as the user needs to be logged in
		self.assertEqual(response.status_code, 302)
		self.client.post(reverse('account'))
		




