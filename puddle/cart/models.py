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
