from django.db import models
from item.models import Item

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total_cost(self):
        total_cost = sum(item.product.price * item.quantity for item in self.cartitem_set.all())
        return total_cost
    
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def get_total_item_cost(self):
        return self.product.price * self.quantity

class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronic_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=14)
    delivery_service = models.CharField(max_length=20, choices=[
        ('novaposhta', 'Нова Пошта'),
        ('ukrposhta', 'Укрпошта'),
    ])
    delivery_address = models.TextField()
    contact_required = models.BooleanField(default=False)

    def get_total_cost(self):
        total_cost = sum(item.product.price * item.quantity for item in self.orderitem_set.all())
        return total_cost

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def get_total_item_cost(self):
        return self.product.price * self.quantity