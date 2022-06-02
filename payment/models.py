from django.db import models

from accounts.models import User
from pricing.models import Pricing

# Create your models here.


class Payment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    pricing = models.ForeignKey(
        Pricing,
        on_delete=models.CASCADE
    )
    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    payment_method = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.pricing}'


class Subscribed(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    pricing = models.ForeignKey(
        Pricing,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    trxid = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.trxid}'


class Withdraw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s withdraw amount {self.amount}"
