from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, ConsultationSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()


from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer

from django.contrib.auth import login, authenticate, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        data = request.data

        if "email" not in data or "password" not in data:
            return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=data["email"]).exists():
            return Response({"error": "Email already in use!"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=data["email"],
            email=data["email"],
            password=data["password"]
        )
        
        login(request, user)  # Automatically log in after registration

        return Response({"message": "User registered and logged in successfully!"}, status=status.HTTP_201_CREATED)
# class LoginView(APIView):
#     def post(self, request):
#         print("Incoming Login Data:", request.data)  # ✅ Debugging

#         email = request.data.get("email")
#         password = request.data.get("password")

#         if not email or not password:
#             print("❌ Missing email or password")
#             return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             user = User.objects.get(email=email)
#             print(f"✅ Found user: {user.email}")  # ✅ Debug user lookup
#         except User.DoesNotExist:
#             print("❌ User not found")
#             return Response({"error": "User not found."}, status=status.HTTP_400_BAD_REQUEST)

#         user = authenticate(request=request, username=email, password=password)

#         if user is not None:
#             print("✅ Authentication successful")
#             return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)

#         print("❌ Invalid credentials")
#         return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)  # Start session
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        logout(request)  # End session
        return Response({"message": "Logged out successfully!"}, status=status.HTTP_200_OK)

    
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        response["Access-Control-Allow-Credentials"] = "true"
        return response
class CheckAuthView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return Response({
                "authenticated": True,
                "user": {
                    "id": request.user.id,
                    "email": request.user.email
                }
            }, status=status.HTTP_200_OK)
        return Response({"authenticated": False}, status=status.HTTP_200_OK)

class LogoutView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id  # Assign logged-in user

        serializer = ConsultationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Consultation submitted successfully!"}, status=status.HTTP_201_CREATED)
        
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.contrib.auth.decorators import login_required

@login_required
def get_user(request):
    if request.user.is_authenticated:
        return JsonResponse({"username": request.user.username})
    return JsonResponse({"error": "User not authenticated"}, status=401)

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

def get_user_data(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=401)
    
    user = request.user
    return JsonResponse({
        "username": user.username,
        "email": user.email
    })

from django.contrib.auth import logout
from django.http import JsonResponse

def logout_view(request):
    logout(request)
    return JsonResponse({"message": "Logged out successfully"}, status=200)