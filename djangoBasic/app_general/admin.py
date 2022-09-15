from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'update', 'show_image_pic']
    search_fields = ['title']
    list_filter = ['title']

# Register your models here.
admin.site.register(Blog, BlogAdmin)