from django.contrib import admin
from faq.models import Faq

# Register your models here.


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug', 'created_at')
    list_filter = ('title',)
    search_fields = ['title']
