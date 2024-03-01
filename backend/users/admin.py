from django.contrib import admin
from .models import User
from django.apps import apps


admin.site.register(User)
