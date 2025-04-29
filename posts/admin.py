from django.contrib import admin
from posts.models import Posts, Category, Tag
# Register your models here.


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'content', 'created_at', 'updated_at', 'rate', 'author']
    list_filter = ['category']
    search_fields = ['title', 'content']
   


admin.site.register(Category)
admin.site.register(Tag)