from django.contrib import admin
from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'patronic_name', 'address', 'get_total_cost', 'created_at_display']
    list_filter = ['created_at']  # 'created_at' should be a DateField or DateTimeField in your Order model
    search_fields = ['first_name', 'last_name', 'address']

    def get_total_cost(self, obj):
        return obj.get_total_cost()

    get_total_cost.short_description = 'Total Cost'  # Set a custom column header

    def created_at_display(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %H:%M:%S')  # Format date and time as needed

    created_at_display.short_description = 'Created At'  # Set a custom column header

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'product', 'quantity', 'get_total_item_cost']
    list_filter = ['order']  # 'order' should refer to a ForeignKey field in your OrderItem model
    search_fields = ['order__first_name', 'order__last_name', 'product__name']

    def get_total_item_cost(self, obj):
        return obj.get_total_item_cost()

    get_total_item_cost.short_description = 'Total Item Cost'  # Set a custom column header

    def order_id(self, obj):
        return obj.order.id  # Display the order ID for each order item

    order_id.short_description = 'Order ID'  # Set a custom column header
