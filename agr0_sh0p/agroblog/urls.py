from django.urls import path

from . import views

app_name = 'agroblog'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<post_id>/edit/', views.post_edit, name='post_edit'),
    path('create/', views.post_create, name='post_create'),
    path(
        'posts/<int:post_id>/comment/',
        views.add_comment, name='add_comment'
    ),
]
