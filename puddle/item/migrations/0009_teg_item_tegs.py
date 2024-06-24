# Generated by Django 5.0.6 on 2024-06-23 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_remove_item_setia_item_seria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Тег',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='item',
            name='tegs',
            field=models.ManyToManyField(blank=True, null=True, related_name='items', to='item.teg'),
        ),
    ]