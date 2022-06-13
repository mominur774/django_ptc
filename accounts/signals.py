from turtle import pos
from django.db.models.signals import post_save
from accounts.models import User, UserReferralCode
from django.dispatch import receiver
import random
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def create_referral_code(sender, instance, created, **kwargs):
    if created:
        UserReferralCode.objects.create(
            user=instance,
            referral_code=instance.first_name+str(random.randint(1000, 9000))
        )


@receiver(post_save, sender=User)
def send_otp(sender, instance, created, **kwargs):
    if created:
        mail_subject = "Verify email"
        mail_message = f"Please verify your email first. Your OTP code is : {instance.otp}"
        to_email = instance.email
        send_mail(
            subject=mail_subject,
            message=mail_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=False
        )
