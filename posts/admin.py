from django.contrib import admin
from posts.models import Posts, Category, Tag
# Register your models here.

admin.site.register(Posts)
admin.site.register(Category)
admin.site.register(Tag)