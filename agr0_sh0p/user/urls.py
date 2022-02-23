from django.urls import path
from django.contrib.auth.views import (
    LogoutView, 
    PasswordChangeView,
    PasswordChangeDoneView,
    )

from . import views

app_name = 'user'

urlpatterns = [
    path(
        'registration/',
        views.user_registr,
        name='registration'
    ),
    path(
        'login/',
        views.user_login,
        name='login'
    ),
    path(
        'user/<str:username>/',
        views.user_page,
        name='user_page'
    ),    
    path(
        'logout/',
        LogoutView.as_view(
            template_name='sales_backend/main_page.html'
        ),
        name='logout'
    ),
    path(
        'password_reset/',
        PasswordChangeView.as_view(
            template_name='user/password_reset.html'
        ),
        name='password_reset'
    ),
    path(
        'password_reset/',
        PasswordChangeDoneView.as_view(
            template_name='user/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
]