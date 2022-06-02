from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class Faq(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = AutoSlugField(populate_from='title', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
