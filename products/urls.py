from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
	path('', views.ProductListView.as_view(), name='all-products'),
	path('<slug:slug>/', views.ProductDetailView.as_view(), name='product-detail'),
	path('category/<slug>/', views.CategoryProductListView.as_view(), name='category-detail'),
]
