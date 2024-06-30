from django.shortcuts import render,get_object_or_404,redirect
from .models import Item,ItemImage,Category,Producer,Teg,Seria
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test

from .forms import ItemWithImagesForm, ItemImageForm,ProducerForm,TegForm,SeriaForm


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


def detail(request, pk):  #зробити для багатьох картинок
    item=get_object_or_404(Item,pk=pk)
    related_items = Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]

    return render(request,'item/detail.html',{
        'item':item,
        'related_items':related_items,
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
