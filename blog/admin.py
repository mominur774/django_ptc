from django.contrib import admin
from blog.models import Blog

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail', 'description', 'slug', 'created_at')
    list_filter = ('title',)
    search_fields = ['title']
