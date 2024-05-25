from django.contrib import admin
from .models import Post, Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'image', 'content', 'status', 'category']


admin.site.register(Post)
admin.site.register(Category)

