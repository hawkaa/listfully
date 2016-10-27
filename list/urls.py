from django.conf.urls import url
from django.conf import settings
from django.views.generic.base import TemplateView
from . import views

# TODO: make server serve images, not djangi url
# TODO: ensure not everyone can fetch all images?
# TODO: add url for fetching images
#from django.views import *
# url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/media/',})

print('MEDIA_ROOT', settings.MEDIA_ROOT)

urlpatterns = [
    url(r'^lists/(\d+)/delete/(\d+)/$', views.delete_item, name='delete_item'),
    url(r'^lists/(\d+)/$', views.add_item, name='items'),
    url(r'^lists/add/$', views.add_list, name='add_list'),
    url(r'^lists/$', TemplateView.as_view(template_name='lists.html'), name='lists'),
    url(r'^profile/$', TemplateView.as_view(template_name='profile.html'), name='profile')
]
