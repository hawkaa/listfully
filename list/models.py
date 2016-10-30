from django.db import models
from django.contrib.auth.models import User as auth_user

def item_image_path(instance, filename):
    return ('item_images/' + filename).format(auth_user.id, instance.id)

# TODO: add hash URL to list for non authenthiced users to use.

class List(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(auth_user)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price_range = models.CharField(max_length=20)
    url = models.CharField(max_length=500, default='')
    image = models.ImageField(upload_to=item_image_path, blank=True)
