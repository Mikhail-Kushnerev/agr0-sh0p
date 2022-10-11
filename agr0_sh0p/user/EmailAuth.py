import email
from .models import User
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

class CustomBackend(ModelBackend):
    def authenticate(
        self,
        request,
        username=None,
        password=None,
        **kwargs
    ):
        try:
            user = User.objects.get(
                Q(email=username) | Q(phone_number=username)
            )
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
