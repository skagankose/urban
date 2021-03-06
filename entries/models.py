# Core
from django.db import models

# Get time
from django.utils import timezone

# Default user model
from django.contrib.auth.models import User

# Entry model
class Entry(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    text = models.TextField()
    up_voters = models.ManyToManyField(User, related_name='up_entries', blank=True)
    down_voters = models.ManyToManyField(User, related_name='down_entries', blank=True)
    rate_up = models.IntegerField(default=0)
    rate_down = models.IntegerField(default=0)
    rate_total = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    edited = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to = 'img/', blank=True)

    def save(self, *args, **kwargs):
        try:
            this = Entry.objects.get(pk=self.pk)
            if this.thumbnail != self.thumbnail and this.thumbnail != 'img/thumbnail.png':
                    this.thumbnail.delete(save=False)
        except: pass       
        super(Entry, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-rate_total']

    def __str__(self):
        return self.title

# Extend default user model
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile')
    website = models.URLField(blank=True)
    avatar = models.ImageField(upload_to = 'img/', blank=True)

    def save(self, *args, **kwargs):
        try:
            this = UserProfile.objects.get(pk=self.pk)
            if this.avatar != self.avatar and this.avatar != 'img/avatar.png':
                this.avatar.delete(save=False)
        except: pass 
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

# Comments of entries
class Comment(models.Model):
    author = models.ForeignKey(User)
    entry = models.ForeignKey(Entry)
    text = models.TextField(max_length=300)
    up_voters = models.ManyToManyField(User, related_name='up_comments', blank=True)
    down_voters = models.ManyToManyField(User, related_name='down_comments', blank=True)
    rate_up = models.IntegerField(default=0)
    rate_down = models.IntegerField(default=0)
    rate_total = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    edited = models.BooleanField(default=False)

    # slug = models.SlugField(unique=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.text)
    #     super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk) + '-' + self.author.username

# Subcomments of comments
class Subcomment(models.Model):
    author = models.ForeignKey(User)
    entry = models.ForeignKey(Entry)
    comment = models.ForeignKey(Comment, related_name='subcomments')
    text = models.TextField(max_length=200)
    up_voters = models.ManyToManyField(User, related_name='up_subcomments', blank=True)
    down_voters = models.ManyToManyField(User, related_name='down_subcomments', blank=True)
    rate_up = models.IntegerField(default=0)
    rate_down = models.IntegerField(default=0)
    rate_total = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    edited = models.BooleanField(default=False)

    class Meta:
        ordering = ['-rate_total']

    def __str__(self):
        return str(self.pk) + '-' + self.author.username

# Twosubcomments of subcomments
class Twosubcomment(models.Model):
    author = models.ForeignKey(User)
    entry = models.ForeignKey(Entry)
    comment = models.ForeignKey(Comment)
    subcomment = models.ForeignKey(Subcomment, related_name='twosubcomments')
    text = models.TextField(max_length=200)
    up_voters = models.ManyToManyField(User, related_name='up_twosubcomments', blank=True)
    down_voters = models.ManyToManyField(User, related_name='down_twosubcomments', blank=True)
    rate_up = models.IntegerField(default=0)
    rate_down = models.IntegerField(default=0)
    rate_total = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    edited = models.BooleanField(default=False)

    class Meta:
        ordering = ['-rate_total']

    def __str__(self):
        return str(self.pk) + '-' + self.author.username
        