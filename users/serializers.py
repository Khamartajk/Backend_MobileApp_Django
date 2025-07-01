from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")

        if not check_password(data['password'], user.password):
            raise serializers.ValidationError("Incorrect password")
        data['user'] = user
        return data
