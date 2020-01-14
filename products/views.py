from django.shortcuts import render, get_object_or_404
from . models import Product
from django.views.generic import DetailView, ListView

def product_category(request, category):
    products = Product.objects.filter(category=category)

    return render(request, "products/product_list.html", {"products": products})

class ProductListView(ListView):
	model = Product
	paginate_by = 2

class ProductDetailView(DetailView):
	model = Product



