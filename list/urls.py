from django.conf.urls import url
from django.conf import settings
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

# TODO: make server serve images (cvontroller), not djangi url

urlpatterns = [
    url(r'^(?P<share>[a-zA-Z0-9]{32})/$', views.share, name='share'),
    url(r'^lists/buy/$', views.buy, name='buy'),
    url(r'^lists/(\d+)/delete/(\d+)/$', views.delete_item, name='delete_item'),
    url(r'^lists/(\d+)/$', views.add_item, name='items'),
    url(r'^lists/add/$', views.add_list, name='add_list'),
    url(r'^lists/$', TemplateView.as_view(template_name='lists.html'), name='lists'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
