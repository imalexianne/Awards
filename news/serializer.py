from rest_framework import serializers
from .models import CoreProject
from .models import CoreProfile

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreProject
        fields = ('id','title', 'description', 'link')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreProfile
        fields = ('id','first_name', 'last_name', 'bio')

        