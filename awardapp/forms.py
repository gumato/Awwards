from django import forms
from .models import Project,Profile

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=250, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
  