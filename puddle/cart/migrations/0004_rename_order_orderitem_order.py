# Generated by Django 4.2.13 on 2024-07-05 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_order_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='Order',
            new_name='order',
        ),
    ]