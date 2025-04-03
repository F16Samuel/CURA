from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

User = get_user_model()

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

# Register Serializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True, required=True)  # Accept `name` field from frontend

    class Meta:
        model = CustomUser
        fields = ["email", "password", "name", "username", "role", "hospital"]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"required": True},
            "username": {"required": False},  # No need to send explicitly from frontend
            "hospital": {"required": False, "allow_blank": True},  # Make hospital optional
        }

    def create(self, validated_data):
        validated_data["username"] = validated_data.pop("name")  # Rename `name` to `username`
        user = CustomUser.objects.create_user(**validated_data)
        return user

# Login Serializer with JWT Token
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        user = authenticate(username=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials")

        return {"user": user}


from rest_framework import serializers
from .models import Consultation

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ['id', 'user', 'name', 'age', 'gender', 'previous_history', 'symptoms', 'created_at']
        read_only_fields = ['user', 'created_at']
