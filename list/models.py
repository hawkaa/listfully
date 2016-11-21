from django.db import models
from django.contrib.auth.models import User as auth_user
from PIL import Image, ExifTags

def item_image_path(instance, filename):
    return ('item_images/' + filename).format(auth_user.id, instance.id)

# TODO: add hash URL to list for non authenthiced users to use.

class List(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(auth_user)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    share = models.CharField(max_length=32, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True)
    price_range = models.CharField(max_length=20, blank=True)
    url = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to=item_image_path, blank=True)
    thumbnail = models.ImageField(upload_to=item_image_path, blank=True)
    bought = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100, blank=True)

    def save(self):
        super(Item, self).save()
        if self.image:
            img = Image.open(self.image.path)

            try:
                for orientation in ExifTags.TAGS.keys():
                  if ExifTags.TAGS[orientation]=='Orientation':
                      break
                exif = dict(img._getexif().items())
                if exif[orientation] == 3:
                  img=img.rotate(180, expand=True)
                  print(3)
                elif exif[orientation] == 6:
                  img=img.rotate(270, expand=True)
                  print(6)
                elif exif[orientation] == 8:
                  img=img.rotate(90, expand=True)
                  print(8)
            except (AttributeError, KeyError, IndexError):
                pass

            base_width = 550
            base = Image.new(mode='RGBA',size=(base_width,base_width),color=(255,255,255,0))
            width, height = img.size

            #SCALE IMAGE
            width_percent = (base_width/float(width))
            new_height = int((float(height)*float(width_percent)))
            img = img.resize((base_width, new_height), Image.ANTIALIAS)
            img.save(self.image.path, 'PNG')

            #CROP HORIZONTAL IMAGES MORE?
            base.paste(img, (0, int((550/2 - img.size[1]/2))))
            base.save(self.thumbnail.path, 'PNG')
