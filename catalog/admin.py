# coding=utf-8
from django.contrib import admin
from .models import CategoryCatalog,Image,Project

class CategoryCatalogAdmin(admin.ModelAdmin):
    list_display = ['name','slug','created','modified']
    search_fields = ['name','slug']
    list_filter = ['created','modified']
    prepopulated_fields = {"slug": ("name",)}

class ImageAdmin(admin.ModelAdmin):
    list_display = ['name','created','modified']
    search_fields = ['name']
    list_filter = ['created','modified']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','slug','created','modified']
    search_fields = ['name','slug']
    list_filter = ['created','modified']
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(CategoryCatalog,CategoryCatalogAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Project,ProjectAdmin)