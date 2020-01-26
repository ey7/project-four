from django.test import TestCase
from django.shortcuts import reverse

class TestSearchPages(TestCase):

	def test_search_template(self):

		response = self.client.get('/search/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'search/search.html')

	def test_search_results_template(self):

		response = self.client.get('/search/results')
		self.assertEqual(response.status_code, 301)

	def category_detail_modern(self):

		response = self.client.get('/search/Modern')
		self.assertEqual(response.status_code, 200)
		self.client.post(reverse('category-detail'))
		self.assertTemplateUsed(response, 'search/categories.html')

	def category_detail_graphite(self):

		response = self.client.get('/search/Graphite')
		self.assertEqual(response.status_code, 200)
		self.client.post(reverse('category-detail'))
		self.assertTemplateUsed(response, 'search/categories.html')

	def category_detail_wood(self):

		response = self.client.get('/search/Wood')
		self.assertEqual(response.status_code, 200)
		self.client.post(reverse('category-detail'))
		self.assertTemplateUsed(response, 'search/categories.html')

	def category_detail_metal(self):

		response = self.client.get('/search/Metal')
		self.assertEqual(response.status_code, 200)
		self.client.post(reverse('category-detail'))
		self.assertTemplateUsed(response, 'search/categories.html')

	def category_detail_oversize(self):
		response = self.client.get('/search/Oversize')
		self.assertEqual(response.status_code, 200)
		self.client.post(reverse('category-detail'))
		self.assertTemplateUsed(response, 'search/categories.html')
		









		






