from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post,Profile

#post creation form
class PostCreateForm(forms.ModelForm):
    class Meta:
        fields=["title","body"]
        model=Post


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        fields=["bio","profile_pic"]
        model=Profile



