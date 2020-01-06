from django.shortcuts import render
from products.models import Product

# Create your views here.

def search(request):
	return render(request, 'search/search.html')

def search_results(request):
    products = Product.objects.filter(title__search=request.GET.get('q'))

    return render(request, "search/search.html", {"products": products})
