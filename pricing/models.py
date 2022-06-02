from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class Pricing(models.Model):
    plan_name = models.CharField(max_length=255)
    amount = models.FloatField()
    earn_per_day = models.IntegerField()
    minimum_withdraw = models.IntegerField()
    ad_limit = models.IntegerField(blank=True, null=True)
    slug = AutoSlugField(populate_from='plan_name', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plan_name


class AdLink(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


class AdLimit(models.Model):
    pricing = models.OneToOneField(Pricing, on_delete=models.CASCADE)
    ad_limit = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pricing} - {self.ad_limit}'
