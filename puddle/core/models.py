
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from cart.models import Cart

class CustomUser(AbstractUser):
    patronymic = models.CharField(max_length=30, blank=True, null=True)
    phone_number=models.CharField(max_length=13, blank=True,null=True)
    adress=models.TextField(null=True)

    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Додайте цей параметр
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Додайте цей параметр
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )
