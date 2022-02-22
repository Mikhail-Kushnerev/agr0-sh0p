from django.contrib import admin

from .models import (
    ProductGroup,
    Product,
    ProductImages,
    CommentProduct
)

class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    raw_id_fields = ['product']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'group',
        'count',
        'price',
        'description',
    )
    search_fields = ('name',)
    # list_filter = ('author', )
    empty_value_display = '-пусто-'
    list_per_page = 20
    inlines = [ProductImagesInline]


admin.site.register(ProductGroup)
admin.site.register(CommentProduct)
