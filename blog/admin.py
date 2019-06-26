from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Post, Tag, Category, Comment

class CategoryAdmin(MPTTModelAdmin):
    """Категории"""
    mptt_level_indent = 20

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)