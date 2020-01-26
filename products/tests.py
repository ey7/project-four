from django.test import TestCase
from . models import Product

class TestProductsPages(TestCase):

	def test_product_list_template(self):
		response = self.client.get('/products/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'products/product_list.html')

	def test_product_detail_template(self):
		product = Product(
			category='graphite',
			title='this is a product title',
			description='description',
			price='500',
			image='graphite.jpg',
			slug='slug'
			)
		product.save()

		response = self.client.get('/products/{}'.format(product.pk))
		self.assertEqual(response.status_code, 301)
		










