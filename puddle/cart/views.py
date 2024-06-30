from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Cart, CartItem
from .forms import CartAddProductForm

def cart_detail(request):
    cart = get_cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

def cart_add(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Item, id=product_id)
    if request.method == 'POST':
        form = CartAddProductForm(request.POST, max_value=product.count)
        if form.is_valid():
            cd = form.cleaned_data
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if created or cd['update']:
                cart_item.quantity = cd['quantity']
            else:
                cart_item.quantity += cd['quantity']
            cart_item.save()
            return redirect('cart/cart_detail.html')
    else:
        form = CartAddProductForm(max_value=product.count)
    return render(request, 'cart/cart_detail.html', {'form': form, 'product': product})


def get_cart(request):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    else:
        cart = Cart.objects.get(id=cart_id)
    return cart

def cart_remove(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Item, id=product_id)
    cart_item = CartItem.objects.filter(cart=cart, product=product).first()
    if cart_item:
        cart_item.delete()
    return redirect('cart:cart_detail')

