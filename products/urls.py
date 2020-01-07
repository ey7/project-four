from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
	path('', views.ProductListView.as_view(), name='all-products'),
	path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
]
