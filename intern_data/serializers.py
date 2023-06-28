from rest_framework import serializers
from .models import InternProfile

class AddInternProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=InternProfile
        fields=['firstname','lastname','email','age','university','profile_photo']

class ViewInternProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=InternProfile
        fields=['firstname','lastname','email','university','profile_photo']
