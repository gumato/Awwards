from django import forms
from .models import Project,Profile

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile','posted_time','user']
  