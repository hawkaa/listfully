from django import forms
from .models import Item, List

class AddItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'url', 'price_range', 'description','image',)

class BuyItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('bought',)

class AddList(forms.ModelForm):
    class Meta:
        model = List
        fields = ('name', 'description', )
