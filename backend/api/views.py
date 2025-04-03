from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=email, password=password)

        if user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        refresh = RefreshToken.for_user(user)

        return Response({
            "message": "Login successful",
            "user": UserSerializer(user).data,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }, status=status.HTTP_200_OK)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
