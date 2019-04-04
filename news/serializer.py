from rest_framework import serializers
from .models import Project

class Project(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'image', 'description', 'link')