from django.test import TestCase

class TestHomePages(TestCase):

	def test_homepage_template(self):

		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'home/index.html')

	def test_about_template(self):

		response = self.client.get('/home/about/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'home/about.html')

	def test_contact_template(self):

		response = self.client.get('/home/contact/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'home/contact.html')

