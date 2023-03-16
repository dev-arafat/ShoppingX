from django.contrib import admin
from .models import (
  Customer,
  Product,
  Cart,
  OrderPlaced
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipCode', 'state']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted', 'brand', 'category', 'product_image']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']


@admin.register(OrderPlaced)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity', 'ordered_date', 'status']