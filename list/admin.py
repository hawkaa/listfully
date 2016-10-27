from django.contrib import admin

from .models import List, Item
from registration.models import RegistrationProfile

admin.site.register(List)
admin.site.register(Item)
