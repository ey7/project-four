from django.contrib import admin
from . models import Product

class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Product, ProductAdmin)
