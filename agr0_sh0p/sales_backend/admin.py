from django.contrib import admin

from .models import ProductGroup, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'group',
        'price',
        'description',
        'count'
    )
    search_fields = ('name',)
    # list_filter = ('author', )
    empty_value_display = '-пусто-'


admin.site.register(ProductGroup)
