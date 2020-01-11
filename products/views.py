from django.shortcuts import render
from . models import Product
from django.views.generic import DetailView, ListView

class ProductListView(ListView):
	model = Product
	paginate_by = 2

class ProductDetailView(DetailView):
	model = Product

def product_category(request, category):
	products = Product.objects.filter(category=category)

	return render(request, "products/product_list.html", {'products': products}) 
