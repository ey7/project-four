from django.db import models
from django.urls import reverse

class Product(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=2)
	image = models.ImageField(upload_to='images')
	slug = models.SlugField(null=False, unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('product-detail', kwargs={'slug': self.slug})
