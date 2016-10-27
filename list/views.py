from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import List, Item
from .forms import AddItem
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
            item.image = request.FILES['image']
            item.save()

            return HttpResponseRedirect('/lists/' + str(list.id))

def delete_item(request, list_id, item_id):
    print("delete")
    instance = Item.objects.get(id=item_id)
    instance.delete()
    return HttpResponseRedirect('/lists/' + str(list_id))

def add_list(request):
    # TODO: continue logic. Ensure to fetch user. Redirect to the list created.
    return HttpResponseRedirect('/lists/')
