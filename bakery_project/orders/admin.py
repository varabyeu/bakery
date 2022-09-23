from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['item']


@admin.register(Order)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'created',
                    'add_to_work', 'completed'
                    ]
    inlines = [OrderItemInline]
