from django import forms
from .models import Item, List

class AddItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'url', 'location', 'price_range', 'description','image', 'id')

class BuyItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('bought',)

class AddList(forms.ModelForm):
    class Meta:
        model = List
        fields = ('name', 'description', )
