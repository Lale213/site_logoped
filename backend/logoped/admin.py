from django.contrib import admin

from .models import *                           # CRUD
admin.site.register(Publication)
admin.site.register(Category)
admin.site.register(Media)
