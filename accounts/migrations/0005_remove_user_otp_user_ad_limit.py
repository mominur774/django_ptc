# Generated by Django 4.0.4 on 2022-05-30 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_checkuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='otp',
        ),
        migrations.AddField(
            model_name='user',
            name='ad_limit',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
