from django.shortcuts import render
from products.models import Product
from django.db.models import Q

# category view
def product_category(request, category):
    products = Product.objects.filter(category=category)

    return render(request, "search/categories.html", {"products": products})

def search(request):
	return render(request, 'search/search.html')

def search_results(request):
	""" code: http://www.learningaboutelectronics.com/Articles/
	How-to-add-search-functionality-to-a-website-in-Django.php"""
	if request.method == 'GET':
		query = request.GET.get('q')

		if query is not None:
			lookups = Q(title__icontains=query) | Q(category__icontains=query)

			results = Product.objects.filter(lookups).distinct()
			results_count = Product.objects.filter(lookups).distinct().count()

			return render(request, "search/search.html",
				{"results": results, "results_count": results_count})
		else:
			return render(request, "search/search.html",
				{"results": results, "results_count": results_count})


