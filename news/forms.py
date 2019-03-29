from django import forms
from .models import Image,Profile,Comments

class ProfileForm(forms.ModelForm):
  
    class Meta:
        model = Profile
        exclude = ['user']

class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        exclude = ['user','profile']

class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        exclude = ['user']

