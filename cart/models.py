from django.db import models
from products.models import Product
import datetime
from django.contrib.auth.models import User

class Order(models.Model):
	"""
	Model to store order information
	"""
	full_name = models.CharField(max_length=50)
	street_address_1 = models.CharField(max_length=50)
	street_address_2 = models.CharField(max_length=50)
	town_or_city = models.CharField(max_length=50)
	county = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	postcode = models.CharField(max_length=10, blank=True)
	date = models.DateField(default=datetime.date.today)
	customer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

	def __str__(self):
		return f'{self.id}-{self.date}-{self.full_name}'

class OrderLineItem(models.Model):
	"""
	Model to store line items, order, product and quantity
	"""
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.PROTECT)
	quantity = models.PositiveIntegerField()

	def __str__(self):
		return f'{self.quantity}-{self.product.title}-{self.product.price}'



