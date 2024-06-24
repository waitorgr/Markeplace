from django.db import models
from django.core.validators import MinValueValidator
from django import forms

class Category(models.Model):
    name= models.CharField(max_length=255)

    class Meta:
        ordering=('name',)
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name
    


class Producer(models.Model):
    name= models.CharField(max_length=255)

    class Meta:
        ordering=('name',)
        verbose_name_plural = 'Виробники'

    def __str__(self):
        return self.name
    
class Seria(models.Model):
    name= models.CharField(max_length=255)
    class Meta:
        ordering=('name',)
        verbose_name_plural = 'Серія'
    def __str__(self):
        return self.name
    
class Teg(models.Model):
    name= models.CharField(max_length=255)
    class Meta:
        ordering=('name',)
        verbose_name_plural = 'Тег'
    def __str__(self):
        return self.name
    

class Item(models.Model):
    image = models.ImageField(upload_to='item_images',blank=True)
    name = models.CharField(max_length=255)
    desctiption = models.TextField(blank=True, null=True)
   
    is_sold= models.BooleanField(default=False)
    
    count = models.IntegerField(validators=[MinValueValidator(0)])
    

    category = models.ForeignKey(Category,related_name='items',on_delete=models.SET_NULL, null=True)
    producer = models.ForeignKey(Producer,related_name='items',on_delete=models.SET_NULL, null=True)
    seria= models.ForeignKey(Seria,related_name='items',on_delete=models.SET_NULL, null=True)
    tegs = models.ManyToManyField(Teg, related_name='items', blank=True, null=True)

    price = models.FloatField()

    class Meta:
        ordering=('name',)
        verbose_name_plural = 'Товари'

    def __str__(self):
        return self.name
    
class ItemImage(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='item_images')

    def __str__(self):
        return f"Image for {self.item.name}"

