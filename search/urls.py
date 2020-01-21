from django.urls import path
from . views import search, search_results, product_category, search_products

app_name = 'search'

urlpatterns = [
	path('', search, name="search"),
	path('results/', search_results, name="search-results"),
	path('<category>/', product_category, name='category-detail'),
	path('products/', search_products, name='products-search'),
]
