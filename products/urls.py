from django.urls import path
from . import views

urlpatterns = [
	path('all-products/', views.ProductListView.as_view(), name='all-products'),
	
]
