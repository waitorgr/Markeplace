# Generated by Django 4.2.13 on 2024-07-05 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_customuser_patronymic_customuser_adress'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='patronymic',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
