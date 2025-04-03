from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, ConsultationSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data

        # Validate required fields
        if "email" not in data or "password" not in data:
            return Response({"error": "Email and Password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if email already exists
        if CustomUser.objects.filter(email=data["email"]).exists():
            return Response({"error": "Email already in use!"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.create(
                username=data["email"],  # Use email as username
                email=data["email"],
                role=data.get("role", "patient"),
                hospital=data.get("hospital", ""),
                password=make_password(data["password"]),  # Hash the password
            )
            user.save()
            return JsonResponse({"success": True, "message": "User registered successfully!"}, status=201)
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)
class LoginView(APIView):
    def post(self, request):
        print("Incoming Login Data:", request.data)  # ✅ Debugging

        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            print("❌ Missing email or password")
            return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            print(f"✅ Found user: {user.email}")  # ✅ Debug user lookup
        except User.DoesNotExist:
            print("❌ User not found")
            return Response({"error": "User not found."}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request=request, username=email, password=password)

        if user is not None:
            print("✅ Authentication successful")
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)

        print("❌ Invalid credentials")
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ConsultationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id  # Assign logged-in user

        serializer = ConsultationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Consultation submitted successfully!"}, status=status.HTTP_201_CREATED)
        
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)