from django.db import models
from django.contrib.auth.models import User as auth_user
from PIL import Image

def item_image_path(instance, filename):
    return ('item_images/' + filename).format(auth_user.id, instance.id)

# TODO: add hash URL to list for non authenthiced users to use.

class List(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(auth_user)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    share = models.CharField(max_length=32, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price_range = models.CharField(max_length=20)
    url = models.CharField(max_length=500, default='')
    image = models.ImageField(upload_to=item_image_path, blank=True)
    bought = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def save(self):
        super(Item, self).save()
        if self.image:
            base_width = 300
            img = Image.open(self.image.path)
            width, height = img.size
            width_percent = (base_width/float(width))
            new_height = int((float(height)*float(width_percent)))
            img = img.resize((base_width, new_height), Image.ANTIALIAS)
            img.save(self.image.path)
