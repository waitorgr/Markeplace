from django import forms

class CartAddProductForm(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    quantity = forms.IntegerField(min_value=1, initial=1, widget=forms.NumberInput(attrs={'class': 'quantity-input'}),label='Кількість')
    def __init__(self, *args, **kwargs):
        self.max_value = kwargs.pop('max_value', None)
        super().__init__(*args, **kwargs)
        if self.max_value is not None:
            self.fields['quantity'].max_value = self.max_value