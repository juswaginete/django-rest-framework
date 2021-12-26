from django.contrib import admin

# Register your models here.
from .models import Products, ProductsType


admin.site.register(Products)
admin.site.register(ProductsType)