from rest_framework import serializers
from .models import RegisterClasses

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterClasses
        fields = '__all__'