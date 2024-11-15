# Generated by Django 5.0.6 on 2024-06-22 20:54

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_alter_item_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Виробники',
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='item',
            name='count',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='item',
            name='producer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.producer'),
        ),
    ]
