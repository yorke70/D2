from django.contrib import admin
from .models import Post, Category, PostCategory


class PostCategoryInLine(admin.TabularInline):
    model = PostCategory
    fk_name = 'post_name'
    extra = 2

class PostAdmin(admin.ModelAdmin):
    inlines = [PostCategoryInLine]


# admin.site.register(Post)
# admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)



