from django import forms
from .models import Project,Profile

class ProfileForm(forms.ModelForm):
  
    class Meta:
        model = Profile
        exclude = ['user']

class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        exclude = ['user','profile']

# class CommentsForm(forms.ModelForm):

#     class Meta:
#         model = Comments
#         exclude = ['user']

