from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls', namespace='user')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', include('sales_backend.urls', namespace='sales_backend')),
    path('', include('sendemail.urls', namespace='sendemail')),
    path('orders/', include('orders.urls', namespace='orders')),   
]

from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
