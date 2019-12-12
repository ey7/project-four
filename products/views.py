from django.shortcuts import render
from . models import Product
from django.views.generic import DetailView, ListView

class ProductListView(ListView):
	model = Product


