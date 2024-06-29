from django.shortcuts import render,redirect, get_object_or_404
from item.models import Category,Item,Producer
from .forms import Signup
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from .models import CustomUser

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

def user_is_admin(user):
    return user.is_superuser

@user_passes_test(user_is_admin)
def admin_page(request):
    return render(request, 'core/admin_page.html')

@user_passes_test(user_is_admin)
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'core/user_list.html', {'users': users})

@user_passes_test(user_is_admin)
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    return redirect('core:user_list')