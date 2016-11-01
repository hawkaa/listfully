from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import List, Item
from .forms import AddItem, AddList
from django.forms import inlineformset_factory
from django.utils.crypto import get_random_string

# TODO: add view for editing profile (firstname, lastname, email, profile picture)
# TODO: add view for creating a new list

def complete_url(url):
    return url.startswith('http')

def random_id_32():
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    return get_random_string(length=32, allowed_chars=characters)


def add_item(request, id):
    list = List.objects.get(pk=id)

    if request.method == 'GET':
        form = AddItem()
        return render(request, '../templates/items.html', {'form': form, 'list': list})

    if request.method == 'POST':
        form = AddItem(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.list = list
            if 'image' in request.FILES:
                print(request.FILES)
                item.image = request.FILES['image']
            item.save()

            return HttpResponseRedirect('/lists/' + str(list.id))

def delete_item(request, list_id, item_id):
    instance = Item.objects.get(id=item_id)
    instance.delete()
    return HttpResponseRedirect('/lists/' + str(list_id))

def add_list(request):
    if request.method == 'GET':
        form = AddList()
        return render(request, '../templates/add_list.html', {'form': form})

    if request.method == 'POST':
        form = AddList(request.POST)
        if form.is_valid():
            list = form.save(commit=False)
            list.user = request.user
            list.share = random_id_32()
            list.save()
            return HttpResponseRedirect('/lists/')

def share(request, share):
    if request.method == 'GET':
        form = BuyItem()
        list = List.objects.get(share=share)
        items = [item.id for item in list.item_set.all().iterator()]

        return render(request, '../templates/share.html', {'form': form, 'list': list, 'items': items})
