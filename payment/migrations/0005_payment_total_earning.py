# Generated by Django 4.0.4 on 2022-05-29 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_payment_ad_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='total_earning',
            field=models.FloatField(default=0.0),
        ),
    ]
