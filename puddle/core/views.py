from django.shortcuts import render,redirect
from django.contrib.auth import login
from item.models import Category,Item,Producer
from .forms import Signup
from django.contrib.auth import logout

def index(request):
    items=Item.objects.filter(is_sold=False)[0:6] #відображення 6 айтемів
    categories = Category.objects.all()
    producers = Producer.objects.all()[0:6]
    return render(request,'core/index.html',{
                  'categories': categories,
                  'items':items,
                  'producers':producers})


def contact(request):
    return render(request,'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  #повертає назад
    else:
        form = Signup()
    return render(request, 'core/signup.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('/')  # Перенаправлення на головну сторінку або іншу, якщо потрібно
