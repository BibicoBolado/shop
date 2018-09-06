# coding=utf-8
from django.contrib import admin
from .models import Post,CategoryBlog

class CategoryBlogAdmin(admin.ModelAdmin):
    list_display    = ['name','created']
    search_fields   = ['name','slug']
    list_filter = ['created','modified']
    prepopulated_fields = {"slug": ("name",)}


class PostAdmin(admin.ModelAdmin):
    list_display = ['name','created','nreads','featured']
    search_fields = ['name','slug']
    list_filter = ['created','modified','featured']
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(CategoryBlog,CategoryBlogAdmin)
admin.site.register(Post,PostAdmin)