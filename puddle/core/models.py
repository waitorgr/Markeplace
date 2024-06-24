
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    patronymic = models.CharField(max_length=30, blank=True, null=True)
    
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
