from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
