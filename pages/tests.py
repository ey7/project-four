from django.test import TestCase

class indexPageTest(TestCase):

	def test_homepage_template(self):

		response = self.client.get('/')
		self.assertTemplateUsed(response, 'index.html')