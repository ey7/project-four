from django.urls import path
from . views import search, search_results

urlpatterns = [
	path('', search, name="search"),
	path('results/', search_results, name="search-results"),
]
