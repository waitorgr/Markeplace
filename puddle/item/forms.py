from django import forms
from .models import Item, ItemImage

class ItemImageForm(forms.ModelForm):
    class Meta:
        model = ItemImage
        fields = ['image']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class ItemWithImagesForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Item
        fields = '__all__'
