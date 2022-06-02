from django.contrib import admin
from contact.models import Contact

# Register your models here.


@admin.register(Contact)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    list_filter = ('email',)
    search_fields = ['email']
