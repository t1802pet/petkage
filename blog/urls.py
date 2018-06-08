from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog_list, name='blog_list'),
    url(r'^create/$', views.blog_create, name='blog_create'),
    url(r'^(?P<post_pk>\d+)/$', views.blog_detail, name='blog_detail'),


]
