from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/create/$', views.post_create, name='post_create'),

]
