# Core
from django import forms
from django.core.files.images import get_image_dimensions

# Default user model
from django.contrib.auth.models import User

# Get time
from django.utils import timezone

# Ours'
from .models import UserProfile, Comment, Entry, Subcomment,Twosubcomment

# User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

# Userprofile 
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'avatar')

# Entry
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'description', 'text', 'thumbnail')

# Edit entry
class UpdateEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'description', 'text', 'thumbnail')

# Edit user
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', )

# Edit userprofile
class UpdateUserProfileForm(forms.ModelForm):    
    class Meta:
        model = UserProfile
        fields = ('avatar',)

# Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

# Edit comment
class EditCommentForm(forms.ModelForm):
    text = forms.CharField(max_length=300, required=False, widget=forms.Textarea)
    class Meta:
        model = Comment
        fields = ('text',)

# Subcomment
class SubcommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5,}))
    class Meta:
        model = Subcomment
        fields = ('text',)

# Edit Subcomment
class EditSubcommentForm(forms.ModelForm):
    text = forms.CharField(max_length=300, required=False, widget=forms.Textarea)
    class Meta:
        model = Subcomment
        fields = ('text',)

# Twosubcomment
class TwosubcommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5,}))
    class Meta:
        model = Twosubcomment
        fields = ('text',)

# Edit Twosubcomment
class EditTwosubcommentForm(forms.ModelForm):
    text = forms.CharField(max_length=300, required=False, widget=forms.Textarea)
    class Meta:
        model = Twosubcomment
        fields = ('text',)
        