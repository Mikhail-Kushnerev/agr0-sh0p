from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from .manager import CustomAccountManager


class User(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    username = models.CharField(
        unique=True,
        max_length=150, 
        null=True,
        blank=True
    )
    email = models.EmailField(
        unique=True,
        null=True,
        blank=True
    )
    phone_number = models.CharField(max_length=12, blank=True)
    # start_date = models.DecimalField(default=timezone.now)
    last_login = models.DateTimeField(auto_now=True)   
    is_admin = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    
    # objects = CustomAccountManager()

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email']

    def __str__(self) -> str:
        return self.username

    # def has_perm(self, perm: str, obj: None) -> bool:
    #     return self.is_admin

    # def has_module_perms(self, app_label: str) -> bool:
    #     return True