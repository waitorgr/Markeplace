from django.contrib import admin

from .models import Category,Item,Producer,ItemImage,Seria,Teg

admin.site.register(Category)

admin.site.register(Producer)
admin.site.register(Seria)
admin.site.register(Teg)

class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 1

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInline]

    list_display = ('name', 'category', 'price', 'is_sold', 'producer', 'count')
    search_fields = ('name', 'category__name', 'producer__name')
    list_filter = ('category', 'is_sold', 'producer')