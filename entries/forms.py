from django import forms

# Default user model
from django.contrib.auth.models import User

# Get time now
from django.utils import timezone

# Ours
from .models import UserProfile, Comment, Entry, Subcomment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website',)

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'description', 'text')

class UpdateEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'description', 'text')

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class EditCommentForm(forms.ModelForm):
    text = forms.CharField(max_length=300, required=False, widget=forms.Textarea)
    class Meta:
        model = Comment
        fields = ('text',)




