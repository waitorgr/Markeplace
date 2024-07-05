from django.shortcuts import render,get_object_or_404,redirect
from .models import Item,ItemImage,Category,Producer,Teg,Seria
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test

from .forms import ItemWithImagesForm, ItemImageForm,ProducerForm,TegForm,SeriaForm,CartAddProductForm
from cart.models import CartItem,Cart


from django.db.models import Q


def items(request):
    items = Item.objects.filter(is_sold=False)

    category_id = request.GET.get('category', 0)
    category_id = int(category_id) if category_id else 0

    producer_id = request.GET.get('producer', 0)
    producer_id = int(producer_id) if producer_id else 0

    seria_id = request.GET.get('seria', 0)
    seria_id = int(seria_id) if seria_id else 0

    teg_ids = request.GET.getlist('teg')
    if teg_ids and isinstance(teg_ids, str):
        teg_ids = teg_ids.split(',')

    tegs = Teg.objects.all()

    query = request.GET.get('query', '')

    sort_by = request.GET.get('sort_by', 'relevance')

    # Фільтрація за категорією
    if category_id:
        items = items.filter(category_id=category_id)

    # Фільтрація за виробником
    if producer_id:
        items = items.filter(producer_id=producer_id)

    # Фільтрація за тегами
    if teg_ids:
        if teg_ids and teg_ids[0] != '':
            teg_ids = list(map(int, teg_ids))
            items = items.filter(tegs__id__in=teg_ids).distinct()

    # Фільтрація за серією
    if seria_id:
        items = items.filter(seria_id=seria_id)

    # Фільтрація за запитом
    if query:
        items = items.filter(Q(name__icontains=query))

    # Сортування
    if sort_by == 'price_asc':
        items = items.order_by('price')
    elif sort_by == 'price_desc':
        items = items.order_by('-price')
    # Релевантність (за замовчуванням)
    elif sort_by == 'relevance':
        pass

    categories = Category.objects.all()
    producers = Producer.objects.all()
    serias = Seria.objects.all()

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'producers': producers,
        'tegs': tegs,
        'serias': serias,
        'category_id': category_id,
        'producer_id': producer_id,
        'teg_ids': teg_ids,
        'seria_id': seria_id,
        'sort_by': sort_by,
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
