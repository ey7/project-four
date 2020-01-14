from django.shortcuts import render, get_object_or_404
from . models import Product
from django.views.generic import DetailView, ListView

class ProductListView(ListView):
	model = Product
	paginate_by = 2

class ProductDetailView(DetailView):
	model = Product

class CategoryListView(ListView):
	model = Product
	template_name = 'products/categories.html'

	def get_queryset(self):
		return Product.objects.filter(category='Graphite')



