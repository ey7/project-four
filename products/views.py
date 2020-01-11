from django.shortcuts import render, get_object_or_404
from . models import Product
from django.views.generic import DetailView, ListView

class ProductListView(ListView):
	model = Product
	paginate_by = 2

class ProductDetailView(DetailView):
	model = Product

class CategoryProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'

    def get_queryset(self):
       category = get_object_or_404(Category, slug=self.kwargs['slug'])
       return super(CategoryProductListView, self).get_queryset().filter(category=category)
