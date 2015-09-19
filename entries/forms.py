from django import forms

# Default user model
from django.contrib.auth.models import User

# Ours
from .models import UserProfile
from .models import Entry

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