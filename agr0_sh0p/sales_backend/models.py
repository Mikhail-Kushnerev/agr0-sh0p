from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
# Create your models here.
from user.models import User


class ProductGroup(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=200)
    group = models.ForeignKey(
        ProductGroup,
        related_name='categroria',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name='product_seller',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        default='default.jpg',
        null=True,
        blank=True,
        upload_to='images/product/'        
    )
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()

    class Meta:
        models.UniqueConstraint(
            fields=['name', 'group', 'user'],
            name='unique_name_group_user'
        )

    def __str__(self) -> str:
        return self.name
