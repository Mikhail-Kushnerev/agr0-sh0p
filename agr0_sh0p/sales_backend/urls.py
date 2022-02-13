from unicodedata import name
from django.urls import path, include

from . import views

app_name = 'sales_backend'

urlpatterns = [
    path('main_page', views.main_page, name='main_page'),
    path('group_list', views.group_list, name='group_list'),
    path('product_detail', views.product_detail, name='product_detail'),
]
