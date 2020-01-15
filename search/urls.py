from django.urls import path
from . views import search, search_results, product_category

urlpatterns = [
	path('', search, name="search"),
	path('results/', search_results, name="search-results"),
	path('<category>/', product_category, name='category-detail'),
]
