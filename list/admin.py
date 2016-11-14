from django.contrib import admin

from .models import List, Item
from registration.models import RegistrationProfile

class ListAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'name')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'list', 'name', 'bought')

admin.site.register(List, ListAdmin)
admin.site.register(Item, ItemAdmin)
