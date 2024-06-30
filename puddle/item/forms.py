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

class CartAddProductForm(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    quantity = forms.IntegerField(min_value=1, initial=1, widget=forms.NumberInput(attrs={'class': 'quantity-input'}),label='Кількість')
    def __init__(self, *args, **kwargs):
        self.max_value = kwargs.pop('max_value', None)
        super().__init__(*args, **kwargs)
        if self.max_value is not None:
            self.fields['quantity'].max_value = self.max_value