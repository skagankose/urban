# Default admin mdel
from django.contrib import admin

# Ours
from .models import Entry, UserProfile, Comment, Comment2


# Populate slug field
class CommentAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug':('text',)}
    pass

# Save our models
admin.site.register(UserProfile)
admin.site.register(Entry)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Comment2)