from django import forms
from .models import Item, ItemImage,Producer,Teg,Seria

class ItemImageForm(forms.ModelForm):
    class Meta:
        model = ItemImage
        fields = ['image']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class ItemWithImagesForm(forms.ModelForm):
    images = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Item
        fields = '__all__'

class ProducerForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = ['name']

class SeriaForm(forms.ModelForm):
    class Meta:
        model = Seria
        fields = ['name']

class TegForm(forms.ModelForm):
    class Meta:
        model = Teg
        fields = ['name']