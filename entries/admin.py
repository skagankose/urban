from django.contrib import admin
from .models import Entry
from .models import UserProfile

admin.site.register(UserProfile)
admin.site.register(Entry)