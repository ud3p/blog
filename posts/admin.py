from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created_at')
admin.site.register(Post, PostAdmin)
# Register your models here.
