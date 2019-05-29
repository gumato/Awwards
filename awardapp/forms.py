from django import forms
from .models import Project,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

class UploadForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'       
  