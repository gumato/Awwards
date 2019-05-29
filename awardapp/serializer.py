from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'bio', 'profile_pic')
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (' image', ' description', 'link',' user')        