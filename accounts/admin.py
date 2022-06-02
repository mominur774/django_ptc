from django.contrib import admin
from accounts.models import User, CheckUser, UserReferralCode

# Register your models here.

admin.site.register(User)
admin.site.register(CheckUser)
admin.site.register(UserReferralCode)
