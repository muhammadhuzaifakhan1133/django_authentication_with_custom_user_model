from rest_framework import serializers
from .models import UserModel

class RegisterAndListUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = UserModel
        fields = ['id', 'name', 'email', 'password', 'dob', 'phone', 'created_at', 'is_superuser']