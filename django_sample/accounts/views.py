from django.shortcuts import render
from django.contrib.auth.views import login as auth_login
# Create your views here.


def login(request):
    return auth_login(request)