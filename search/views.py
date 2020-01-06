from django.shortcuts import render
from products.models import Product
from django.db.models import Q

# Create your views here.

def search(request):
	return render(request, 'search/search.html')

def search_results(request):
	""" code: http://www.learningaboutelectronics.com/Articles/
	How-to-add-search-functionality-to-a-website-in-Django.php"""
	if request.method == 'GET':
		query = request.GET.get('q')

		if query is not None:
			lookups = Q(title__icontains=query) | Q(description__icontains=query)

			results = Product.objects.filter(lookups).distinct()

			return render(request, "search/search.html", {"results": results})
		else:
			return render(request, "search/search.html")
