from django import forms
from django.core.files.images import get_image_dimensions

# Default user model
from django.contrib.auth.models import User

# Get time now
from django.utils import timezone

# Ours
from .models import UserProfile, Comment, Entry, Subcomment,Twosubcomment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'avatar')

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'description', 'text', 'thumbnail')

class UpdateEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'description', 'text', 'thumbnail')

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', )

class UpdateUserProfileForm(forms.ModelForm):    
    class Meta:
        model = UserProfile
        fields = ('avatar',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class EditCommentForm(forms.ModelForm):
    text = forms.CharField(max_length=300, required=False, widget=forms.Textarea)
    class Meta:
        model = Comment
        fields = ('text',)

class SubcommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5,}))
    class Meta:
        model = Subcomment
        fields = ('text',)

class EditSubcommentForm(forms.ModelForm):
    text = forms.CharField(max_length=300, required=False, widget=forms.Textarea)
    class Meta:
        model = Subcomment
        fields = ('text',)

class TwosubcommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5,}))
    class Meta:
        model = Twosubcomment
        fields = ('text',)

class EditTwosubcommentForm(forms.ModelForm):
    text = forms.CharField(max_length=300, required=False, widget=forms.Textarea)
    class Meta:
        model = Twosubcomment
        fields = ('text',)




