from django.contrib.auth.models import BaseUserManager


class CustomAccountManager(BaseUserManager):

    use_in_migrations = True

#     def create_superuser(
#         self,
#         email,
#         username,
#         # first_name,
#         password,
#         # **other_fields        
#     ):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             username=username,
#             password=password
#         )
#         user.is_admin = True
#         user.staff = True
#         user.is_superuser = True
#         user.save()
#         return user


    def create_user(
        self,
        email,
        username,
        # first_name,
        password=None,
        # **other_fields
    ):
        if not email:
            raise ValueError('You must provide an email address')
        if not username:
            raise ValueError('You must have a username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            # first_name=first_name,
            # **other_fields
        )
        user.set_password(password)
        user.save()
        return user