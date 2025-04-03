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
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
import json
from .models import ConsultationReport

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
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User  # Import User model
from api.models import CustomUser  # Change to your custom user model if using one
from django.contrib.auth.hashers import make_password

from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print("Request Data:", request.data)  # Log the incoming data

        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        user_type = request.data.get("user_type")
        hospital = request.data.get("hospital")  # This is for doctors only

        if not username or not email or not password or not user_type:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        if user_type == "doctor" and not hospital:
            return Response({"error": "Hospital is required for doctors"}, status=status.HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(email=email).exists():
            return Response({"error": "Email already in use"}, status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.create(
            username=username,
            email=email,
            password=make_password(password),
            user_type=user_type,
            hospital=hospital if user_type == "doctor" else None  # Set hospital only for doctors
        )

        return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)


class CSRFTokenView(APIView):
    def get(self, request):
        return Response({"csrftoken": get_token(request)})
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

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password

User = get_user_model()  # ✅ Get custom user model

class LoginView(APIView):
    authentication_classes = []  # ✅ No authentication required for login
    permission_classes = [AllowAny]  # ✅ Allow all users to access

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        # ✅ Get user by email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Invalid email or password"}, status=400)

        # ✅ Check password manually
        if not check_password(password, user.password):
            return Response({"error": "Invalid email or password"}, status=400)

        # ✅ Generate or retrieve the token
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
            "user": {
                "id": user.id,
                "name": user.username,  # Use `.first_name` if needed
                "email": user.email
            }
        })

from django.contrib.auth import logout
from django.http import JsonResponse

from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt

def csrf_token_view(request):
    token = get_token(request)
    return JsonResponse({"csrfToken": token})  # ✅ Sends CSRF token to frontend

@csrf_exempt  # 🚨 Debugging only, remove later
def logout_view(request):
    if request.method == "POST":
        logout(request)
        response = JsonResponse({"message": "Logged out successfully"})
        response.delete_cookie("sessionid")  # ✅ Ensure session is cleared
        return response
    return JsonResponse({"error": "Invalid request"}, status=400)



    
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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout

class LogoutView(APIView):
    def post(self, request):
        # Perform logout
        logout(request)
        
        # Clear session data
        request.session.flush()
        
        return Response({"success": True, "message": "Logout successful"}, status=status.HTTP_200_OK)

    

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

from .models import ConsultationReport

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ConsultationReport

@csrf_exempt
def save_consultation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get("user_id", None)
            responses = data.get("responses", {})
            ml_result = data.get("mlResult", "Not Available")

            # Save data in the database
            report = ConsultationReport.objects.create(
                user_id=user_id,
                responses=responses,
                ml_result=ml_result
            )

            return JsonResponse({"message": "Consultation saved successfully!", "report_id": report.id}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=405)


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json
from .models import ConsultationReport

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from .models import ConsultationReport

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from .models import ConsultationReport

def generate_pdf(request, report_id):
    try:
        # Fetch the report data from the database
        report = ConsultationReport.objects.get(id=report_id)

        # Create an HTTP response with a PDF file
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="consultation_report_{report_id}.pdf"'

        # Create PDF document
        doc = SimpleDocTemplate(response, pagesize=letter)
        elements = []
        styles = getSampleStyleSheet()

        # **CURA Web App Header**
        cura_header = Paragraph("<font size=16 color='blue'><b>CURA - Health Consultation Platform</b></font>", styles['Title'])
        elements.append(cura_header)
        elements.append(Spacer(1, 12))

        # **Report Title**
        title = Paragraph("<font size=14><b>Consultation Report</b></font>", styles['Title'])
        elements.append(title)
        elements.append(Spacer(1, 6))

        # **Horizontal Line Separator**
        elements.append(Paragraph("<hr/>", styles["Normal"]))
        elements.append(Spacer(1, 12))

        # **Basic Information (Fixing Bold Formatting)**
        user_info = [
            [Paragraph("<b>Report ID:</b>", styles["Normal"]), str(report.id)],
            [Paragraph("<b>User ID:</b>", styles["Normal"]), str(report.user_id)],
            [Paragraph("<b>ML Diagnosis:</b>", styles["Normal"]), str(report.ml_result)],
        ]

        table = Table(user_info, colWidths=[150, 300])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ]))
        elements.append(table)
        elements.append(Spacer(1, 12))

        # **User Responses Table**
        if report.responses:
            response_data = [
                [Paragraph("<b>Question</b>", styles["Normal"]), Paragraph("<b>Answer</b>", styles["Normal"])]
            ] + [[Paragraph(q, styles["Normal"]), Paragraph(a, styles["Normal"])] for q, a in report.responses.items()]

            response_table = Table(response_data, colWidths=[250, 250])
            response_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ]))
            elements.append(Paragraph("<b>User Responses:</b>", styles["Heading2"]))
            elements.append(Spacer(1, 6))
            elements.append(response_table)

        # **Footer**
        elements.append(Spacer(1, 20))
        footer = Paragraph("<font size=10 color='black'><b>Thanks for using CURA! Stay healthy.</b></font>", styles["Normal"])
        elements.append(footer)

        # Build PDF
        doc.build(elements)
        return response

    except ConsultationReport.DoesNotExist:
        return HttpResponse("Report not found", status=404)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)

