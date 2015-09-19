from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Entry(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    text = models.TextField()
    rate_up = models.IntegerField(default=0)
    rate_down = models.IntegerField(default=0)
    rate_total = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    up_voters = models.ManyToManyField(User, related_name='up_entries', blank=True)
    down_voters = models.ManyToManyField(User, related_name='down_entries', blank=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):

    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    # picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username