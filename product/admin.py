from django.contrib import admin

# Import Models Here
from .models import *

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status', 'created', 'updated']
    list_filter = ['title']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'amount', 'created', 'updated']
    list_filter = ['category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
