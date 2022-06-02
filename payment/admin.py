from django.contrib import admin
from payment.models import Payment, Subscribed, Withdraw

# Register your models here.


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'pricing', 'fullname',
                    'phone_number', 'payment_method')
    list_filter = ('user', 'pricing', 'payment_method')
    search_fields = ['user']


@admin.register(Subscribed)
class SubscribedAdmin(admin.ModelAdmin):
    list_display = ('user', 'pricing', 'trxid')
    list_filter = ('user', 'trxid')
    search_fields = ['user', 'trxid']


@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'paid')
    list_filter = ('paid', )
    search_fields = ['user', 'paid']
