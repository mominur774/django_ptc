from django.contrib import admin
from pricing.models import Pricing, AdLink, AdLimit

# Register your models here.


@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'amount', 'earn_per_day',
                    'minimum_withdraw', 'slug')
    list_filter = ('plan_name', 'amount',)
    search_fields = ['plan_name']


@admin.register(AdLink)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('url', )


@admin.register(AdLimit)
class LimitAdmin(admin.ModelAdmin):
    list_display = ('pricing', 'ad_limit')
