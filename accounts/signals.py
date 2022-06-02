from django.db.models.signals import post_save
from accounts.models import User, UserReferralCode
from django.dispatch import receiver
import random


@receiver(post_save, sender=User)
def create_referral_code(sender, instance, created, **kwargs):
    if created:
        UserReferralCode.objects.create(
            user=instance,
            referral_code=instance.first_name+str(random.randint(1000, 9000))
        )
