from django.shortcuts import render,get_object_or_404,redirect
from .models import Item,ItemImage,Category,Producer,Teg,Seria
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test

from .forms import ItemWithImagesForm, ItemImageForm,ProducerForm,TegForm,SeriaForm,CartAddProductForm
from cart.models import CartItem,Cart


def items(request):
    items= Item.objects.filter(is_sold=False)

    category_id = request.GET.get('category', 0)
    categories= Category.objects.all()

    producer_id = request.GET.get('producer', 0)
    producer= Producer.objects.all()

    teg_ids = request.GET.getlist('teg')
    teg= Teg.objects.all()

    seria_id = request.GET.get('seria', 0)
    seria= Seria.objects.all()

    query= request.GET.get('query','')

    if category_id:
        items = items.filter(category_id=category_id)

    if producer_id:
        items = items.filter(producer_id=producer_id)

    if teg_ids:
        if teg_ids and teg_ids[0] != '':
            teg_ids = list(map(int, teg_ids))
            items = items.filter(tegs__id__in=teg_ids).distinct()

    if seria_id:
        items = items.filter(seria_id=seria_id)

    if query:
        items = items.filter(Q(name__icontains=query) )

    return render(request,'item/items.html',{
        'items':items,
        'query':query,
        'categories':categories,
        'producer':producer,
        'teg':teg,
        'seria':seria,
        'category_id':int(category_id),
        'producer_id':int(producer_id),
        'teg_ids': teg_ids,
        'seria_id':int(seria_id),
    })


def get_cart(request):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    else:
        cart = Cart.objects.get(id=cart_id)
    return cart


def detail(request, pk):  #зробити для багатьох картинок
    item=get_object_or_404(Item,pk=pk)
    related_items = Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]

    cart = get_cart(request)
    if request.method == 'POST':
        form = CartAddProductForm(request.POST, max_value=item.count)
        if form.is_valid():
            cd = form.cleaned_data
            
            # Check if requested quantity exceeds available stock
            if cd['quantity'] > item.count:
                form.add_error('quantity', 'Неможе біти більше ніж є в наявності')
            else:
                cart_item, created = CartItem.objects.get_or_create(cart=cart, product=item)
                if created or cd['update']:
                    cart_item.quantity = cd['quantity']
                else:
                    cart_item.quantity += cd['quantity']
                cart_item.save()
                return redirect('cart:cart_detail')
    else:
        form = CartAddProductForm(max_value=item.count)

    return render(request,'item/detail.html',{
        'item':item,
        'related_items':related_items,
        'form': form, 
    })


def user_is_admin(user):
    return user.is_superuser

@user_passes_test(user_is_admin)
def new(request):
    if request.method == 'POST':
        form = ItemWithImagesForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            images = request.FILES.getlist('images')
            for image in images:
                ItemImage.objects.create(item=item, image=image)
            return redirect('/')  # Замість 'some_view_name' вставте ім'я потрібного вам представлення
    else:
        form = ItemWithImagesForm()
    return render(request, 'item/form.html', {
        'form': form
    })
