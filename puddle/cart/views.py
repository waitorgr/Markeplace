from django.shortcuts import render,redirect, get_object_or_404

from .models import Item, Cart, CartItem,OrderItem,Order
from .forms import CartAddProductForm,OrderForm

from django.contrib import messages
from django.views.generic import ListView,DetailView

def cart_detail(request):
    cart = get_cart(request)

    # Перевірка кількості товарів у кошику перед відображенням
    for cart_item in cart.cartitem_set.all():
        if cart_item.quantity > cart_item.product.count:
            cart_item.quantity = cart_item.product.count
            cart_item.save()
            messages.warning(request, f"Кількість товару '{cart_item.product.name}' була зменшена до наявної кількості.")

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            order = Order.objects.create(
                first_name=cd['first_name'],
                last_name=cd['last_name'],
                patronic_name=cd['patronic_name'],
                address=cd['address'],
                delivery_service=cd['delivery_service'],
                delivery_address=cd['delivery_address'],
                contact_required=cd['requires_contact'],
                phone_number=cd['phone_number']
            )

            # Додавання елементів з кошика до замовлення
            for cart_item in cart.cartitem_set.all():
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity
                )

            # Очищення кошика після створення замовлення та елементів замовлення
            cart.cartitem_set.all().delete()

            return redirect('/')  # Перенаправлення на підходящий URL після успішного оформлення замовлення
    else:
        form = OrderForm()

    return render(request, 'cart/cart_detail.html', {'cart': cart, 'form': form})


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
            return redirect('cart:cart_detail')
    else:
        form = CartAddProductForm(max_value=product.count)

    return render(request, 'cart/cart_detail.html', {'form': form, 'product': product})


def get_cart(request):
    cart_id = request.session.get('cart_id')
    
    # Перевірка, чи користувач авторизований
    if request.user.is_authenticated:
        # Отримання кошика користувача, якщо він існує
        cart = request.user.cart
        # Оновлення сесії з ідентифікатором кошика користувача
        request.session['cart_id'] = cart.id
    else:
        # Створення нового кошика, якщо ідентифікатор не існує в сесії
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

class OrderListView(ListView):
    model = Order
    template_name = 'cart/order_list.html'  # Шлях до шаблону, який ви створите нижче
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'cart/order_detail.html'  # Шлях до шаблону, який ви створите нижче
    context_object_name = 'order'
