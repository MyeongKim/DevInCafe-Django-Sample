from django.contrib import admin
from blog.models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin);