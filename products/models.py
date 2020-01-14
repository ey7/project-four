from django.db import models
from django.urls import reverse

class Product(models.Model):
	GRAPHITE = 'Graphite'
	MODERN = 'Modern'
	METAL = 'Metal'
	OVERSIZE = 'Oversize'
	WOOD = 'Wood'

	CATEGORY_GROUPS = [
		(GRAPHITE, 'Graphite'),
		(MODERN, 'Modern'),
		(METAL, 'Metal'),
		(OVERSIZE, 'Oversize'),
		(WOOD, 'Wood'),
	]
	category = models.CharField(max_length=50, default='', choices=CATEGORY_GROUPS) 
	title = models.CharField(max_length=100)
	description = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=2)
	image = models.ImageField(upload_to='images')
	slug = models.SlugField(null=False, unique=True)

	def __str__(self):
		return f'{self.title}'

	def get_absolute_url(self):
		return reverse('products:product-detail', kwargs={'slug': self.slug})
