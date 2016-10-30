from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import List, Item
from .forms import AddItem, AddList
from django.forms import inlineformset_factory

# TODO: add view for editing profile (firstname, lastname, email, profile picture)
# TODO: add view for creating a new list

def complete_url(url):
    return url.startswith('http')

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
    print("delete")
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
            list.save()
            return HttpResponseRedirect('/lists/')
