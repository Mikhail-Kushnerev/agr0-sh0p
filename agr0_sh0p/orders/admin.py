from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Order, OrderItem, Message, Chat

# @admin.register(Order)
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'address',
        'user',
        'postal_code',
        'city',
        'paid',
        'created',
        'updated'
    ]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

# admin.site.register(Order, OrderAdmin)

admin.site.register(Chat)
admin.site.register(Message)