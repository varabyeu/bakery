from django.contrib import admin
from .models import Category, Product, Images


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    prepopulated_fields = {
        'slug': ('category_name',)
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'product_name', 'category', 'price',
        'is_new', 'is_active', 'created', 'mass'
    ]
    list_filters = [
        'category', 'price', 'product_name', 'is_new',
        'is_active', 'created',
    ]
    list_editable = [
        'price', 'is_new', 'is_active',
    ]
    list_display_links = ['product_name', ]


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = [
        'image_name', 'slug', 'image', 'added',
    ]
    readonly_fields = ('show_in_admin',)

    def show_in_admin(self, obj):
        return obj.show_in_admin

    show_in_admin.short_description = 'Preview'
    show_in_admin.allow_tags = True
