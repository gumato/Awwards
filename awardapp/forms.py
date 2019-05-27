from django import forms
from .models import Project,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=250, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
  