from django.shortcuts import render, get_object_or_404
from . models import Product
from django.views.generic import DetailView, ListView

class ProductListView(ListView):
	model = Product

class ProductDetailView(DetailView):
	model = Product

def product_detail_view(request, primary_key):
    product = get_object_or_404(Product, pk=primary_key)
    return render(request, 'products/product_detail.html', context={'product': product})


