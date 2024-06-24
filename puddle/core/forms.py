from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import CustomUser 

class Signup(UserCreationForm):
    username=forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={
        'placeholder':"Створіть ваше ім'я корстувача"
    }) )
    first_name = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={
        'placeholder':"Введіть ваше ім'я"
    }) )
    last_name = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={
        'placeholder':"Введіть ваше прізвище"
    }) )
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'placeholder':"Введіть ваш email"
    }) )
    patronymic = forms.CharField(required=False, max_length=30, widget=forms.TextInput(attrs={
        'placeholder':"Введіть ваше по батькові"
    }) )

    password1=forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={
        'placeholder':"Введіть ваш пароль"
    }) )

    password2=forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={
        'placeholder':"Повторіть ваш пароль"
    }) )

    
    class Meta:
        model = CustomUser
        fields = ( 'username','first_name', 'last_name','patronymic', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.patronymic = self.cleaned_data['patronymic']  # Добавьте это поле, если у вас есть кастомная модель пользователя
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username=forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={
        'placeholder':"Створіть ваше ім'я корстувача"
    }) )
    password=forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={
        'placeholder':"Введіть ваш пароль"
    }) )