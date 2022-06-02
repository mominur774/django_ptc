
from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import Manager


class User(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=15, unique=True)
    is_phone_verified = models.BooleanField(default=False)
    is_subscribed = models.BooleanField(default=False)
    ad_limit = models.IntegerField(blank=True, null=True)
    total_earning = models.FloatField(default=0.0)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = Manager()

    def __str__(self):
        return self.phone_number

    def full_name(self):
        return self.first_name + self.last_name


class CheckUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    transaction_screenshot = models.ImageField(upload_to="transaction")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s transaction screenshot"


class UserReferralCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    referral_code = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.user}'s referral code - {self.referral_code}"
