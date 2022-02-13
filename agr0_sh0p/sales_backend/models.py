from email.headerregistry import Group
from email.mime import image
from turtle import title
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MetaGroup(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class ProductGroup(models.Model):
    name = models.CharField(max_length=200)
    group = models.ForeignKey(
        MetaGroup,
        related_name='categroria',
        on_delete=models.CASCADE
    )
    # image = models.ImageField
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()

    def __str__(self) -> str:
        return self.name
