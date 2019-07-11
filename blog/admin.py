from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Post, Tag, Category, Comment

class CategoryAdmin(MPTTModelAdmin):
    """Категории"""
    mptt_level_indent = 20

class CommentInLine(admin.TabularInline):
    """Связь коментариев со статьей (StackedInLine - другой вид)"""
    model = Comment
    extra = 2


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created", "publish_date", "active", "sort", "view", "category")
    list_display_links = ("title",)
    list_filter = ("category", "created")
    list_editable = ("sort", "active")
    search_fields = ("title",)
    inlines = [CommentInLine]
    readonly_fields = ("view",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
#admin.site.register(Tag)
admin.site.register(Category, CategoryAdmin)
#admin.site.register(Comment)
# @admin.register(Post)



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

"""
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "active")
    list_filter = ("active",)
    list_editable = ("active",)
    prepopulated_fields = {"slug": ("title",)}
"""


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "moderation")
    list_editable = ("moderation",)