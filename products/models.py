from django.db import models
from django.urls import reverse

category_groups = (

	('Graphite', 'Graphite'),
	('Modern', 'Modern'),
	('Metal', 'Metal'),
	('Oversize', 'Oversize'),
	('Modern', 'Modern'),
	
)

class Category(models.Model):
	name = models.CharField(max_length=100, choices=category_groups, default='Graphite')
	slug = models.SlugField(null=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

		def __str__(self):
			return self.name

class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.PROTECT)
	title = models.CharField(max_length=100)
	description = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=2)
	image = models.ImageField(upload_to='images')
	slug = models.SlugField(null=False, unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('products:product-detail', kwargs={'slug': self.slug})
