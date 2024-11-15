# Generated by Django 4.2.13 on 2024-07-07 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_rename_order_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='contact_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_address',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_service',
            field=models.CharField(choices=[('novaposhta', 'Нова Пошта'), ('ukrposhta', 'Укрпошта')], default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default=0, max_length=14),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
