from django.shortcuts import render,get_object_or_404,redirect
from .models import Item,ItemImage
from django.contrib.auth.decorators import user_passes_test

from .forms import ItemWithImagesForm, ItemImageForm,ProducerForm,TegForm,SeriaForm

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
