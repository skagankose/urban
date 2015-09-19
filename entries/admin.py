# Default admin mdel
from django.contrib import admin

# Ours
from .models import Entry
from .models import UserProfile

# Save our models
admin.site.register(UserProfile)
admin.site.register(Entry)