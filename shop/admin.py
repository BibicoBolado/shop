# coding=utf-8
from django.contrib import admin
from .models import CategoryShop,Product

class CategoryShopAdmin(admin.ModelAdmin):
    list_display = ['name','slug','created','modified']
    search_fields = ['name','slug']
    list_filter = ['created','modified']
    prepopulated_fields = {"slug": ("name",)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category','created','featured']
    search_fields = ['name','slug']
    list_filter = ['created','modified','featured']
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(CategoryShop,CategoryShopAdmin)
admin.site.register(Product,ProductAdmin)