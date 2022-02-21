from unicodedata import name
from django.urls import path, include

from . import views

app_name = 'sales_backend'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('product_group/<slug:slug>/', views.product_group, name='product_group'),
    path(
        'product_detail/<int:id>/',
        views.product_detail,
        name='product_detail'
    ),
    path('create/', views.create_product, name='create_product'),
    path(
        'product_detail/<int:id>/edit/',
        views.edit_product,
        name='edit_product'
    ),
    path(
        'product_detail/<int:id>/comments/',
        views.addcomment,
        name='addcomment'
    ),
]
