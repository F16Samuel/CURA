from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, ConsultationReportSerializer
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

import logging

import json
import logging
from django.http import JsonResponse
from .models import ConsultationReport
from django.views.decorators.csrf import csrf_exempt

def save_consultation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            logging.info(f"Received data: {data}")  # Log received data for debugging

            user_id = data.get("user_id", None)
            responses = data.get("responses", {})
            ml_result = data.get("mlResult", "Not Available")

            # Additional validation logs
            logging.info(f"User ID: {user_id}")
            logging.info(f"Responses: {responses}")
            logging.info(f"ML Result: {ml_result}")

            # Save data in the database
            report = ConsultationReport.objects.create(
                user_id=user_id,
                responses=responses,
                ml_result=ml_result
            )

            return JsonResponse({"message": "Consultation saved successfully!", "report_id": report.id}, status=201)

        except Exception as e:
            logging.error(f"Error saving consultation: {str(e)}")
            return JsonResponse({"error": str(e)}, status=400)



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

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch
from django.http import HttpResponse
from .models import ConsultationReport

def generate_pdf(request, report_id):
    try:
        # Fetch the report data from the database
        report = ConsultationReport.objects.get(id=report_id)

        # Create an HTTP response with a PDF file
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="consultation_report_{report_id}.pdf"'

        # Define modern color scheme
        primary_color = colors.HexColor('#1E88E5')  # Modern blue
        secondary_color = colors.HexColor('#43A047')  # Modern green
        text_color = colors.HexColor('#212121')  # Near black
        light_bg = colors.HexColor('#F5F5F5')  # Very light gray

        # Create PDF document with margins
        doc = SimpleDocTemplate(
            response, 
            pagesize=letter,
            topMargin=0.5*inch,
            bottomMargin=0.5*inch,
            leftMargin=0.75*inch,
            rightMargin=0.75*inch
        )
        
        elements = []
        styles = getSampleStyleSheet()

        # Create custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Title'],
            fontSize=24,
            textColor=primary_color,
            spaceAfter=16,
            alignment=1  # Center alignment
        )
        
        subtitle_style = ParagraphStyle(
            'CustomSubtitle',
            parent=styles['Heading2'],
            fontSize=18,
            textColor=secondary_color,
            spaceAfter=12
        )
        
        # Modified section_title style to ensure it's not italicized
        section_title = ParagraphStyle(
            'SectionTitle',
            parent=styles['Heading3'],
            fontSize=14,
            textColor=text_color,
            spaceBefore=12,
            spaceAfter=6,
            fontName='Helvetica-Bold',  # Using regular bold font instead of potentially italic
            italic=0  # Explicitly setting italic to 0 (off)
        )
        
        body_text = ParagraphStyle(
            'BodyText',
            parent=styles['Normal'],
            fontSize=10,
            textColor=text_color,
            leading=14
        )

        # Header with modern styling
        cura_header = Paragraph(
            "<font color='#1E88E5'><b>CURA</b></font> <font color='#43A047'>Health Consultation</font>",
            title_style
        )
        elements.append(cura_header)
        
        # Report subtitle
        report_title = Paragraph(
            f"Consultation Report #{report.id}",
            subtitle_style
        )
        elements.append(report_title)
        
        # Date & time info
        if hasattr(report, 'created_at'):
            date_info = Paragraph(
                f"Generated on: {report.created_at.strftime('%B %d, %Y at %H:%M')}",
                body_text
            )
            elements.append(date_info)
        
        elements.append(Spacer(1, 20))
        
        # Horizontal separator
        separator_style = TableStyle([
            ('LINEBELOW', (0, 0), (-1, 0), 1, primary_color),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 0),
        ])
        separator = Table([['']],  colWidths=[7*inch])
        separator.setStyle(separator_style)
        elements.append(separator)
        elements.append(Spacer(1, 20))

        # Basic Information Section with modern table - non-italicized section title
        elements.append(Paragraph("Report Summary", section_title))
        elements.append(Spacer(1, 6))
        
        user_info = [
            [Paragraph("<b>Report ID:</b>", body_text), Paragraph(str(report.id), body_text)],
            [Paragraph("<b>ML Diagnosis:</b>", body_text), Paragraph(str(report.ml_result), body_text)],
        ]

        # Modern table with clean styling
        table = Table(user_info, colWidths=[2*inch, 4.5*inch])
        table.setStyle(TableStyle([ 
            # Headers
            ('BACKGROUND', (0, 0), (0, -1), light_bg),
            ('TEXTCOLOR', (0, 0), (0, -1), text_color),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            # Content
            ('BACKGROUND', (1, 0), (1, -1), colors.white),
            # Border styling
            ('GRID', (0, 0), (-1, -1), 0.5, colors.lightgrey),
            # Padding
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ]))
        elements.append(table)
        elements.append(Spacer(1, 30))

        # User Responses Section with modern styling - non-italicized section title
        if report.responses:
            elements.append(Paragraph("Consultation Responses", section_title))
            elements.append(Spacer(1, 6))
            
            # Create enhanced header row
            response_data = [
                [Paragraph("<b>Question</b>", body_text), 
                 Paragraph("<b>Response</b>", body_text)]
            ]
            
            # Add each Q&A row with enhanced styling
            for q, a in report.responses.items():
                question_text = Paragraph(q, body_text)
                answer_text = Paragraph(a, body_text)
                response_data.append([question_text, answer_text])

            response_table = Table(response_data, colWidths=[3.25*inch, 3.25*inch])
            
            # Create dynamic alternating row styles
            table_style = [
                # Header styling
                ('BACKGROUND', (0, 0), (-1, 0), primary_color),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                # Grid styling
                ('GRID', (0, 0), (-1, -1), 0.5, colors.lightgrey),
                # Padding
                ('TOPPADDING', (0, 0), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ('LEFTPADDING', (0, 0), (-1, -1), 12),
                ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ]
            
            # Add alternating row colors dynamically based on available rows
            for i in range(1, len(response_data)):
                if i % 2 == 0:  # Even rows (starting from 1-based index)
                    table_style.append(('BACKGROUND', (0, i), (-1, i), light_bg))
                else:  # Odd rows
                    table_style.append(('BACKGROUND', (0, i), (-1, i), colors.white))
            
            response_table.setStyle(TableStyle(table_style))
            elements.append(response_table)
            elements.append(Spacer(1, 30))

        # Add disclaimer
        disclaimer_style = ParagraphStyle(
            'Disclaimer',
            parent=styles['Italic'],
            fontSize=8,
            textColor=colors.grey,
            alignment=1  # Center alignment
        )
        disclaimer = Paragraph(
            "This report is computer-generated and may require review by a healthcare professional. "
            "CURA's ML diagnosis is not a substitute for professional medical advice.",
            disclaimer_style
        )
        elements.append(disclaimer)
        elements.append(Spacer(1, 12))
        
        # Modern footer with separator
        footer_separator = Table([['']],  colWidths=[7*inch])
        footer_separator.setStyle(TableStyle([
            ('LINEABOVE', (0, 0), (-1, 0), 0.5, colors.lightgrey),
            ('TOPPADDING', (0, 0), (-1, 0), 0),
        ]))
        elements.append(footer_separator)
        
        footer_style = ParagraphStyle(
            'Footer',
            parent=styles['Normal'],
            fontSize=9,
            textColor=secondary_color,
            alignment=1  # Center alignment
        )
        footer = Paragraph(
            "Thank you for using <b>CURA</b> Health Consultation Platform | Stay Healthy",
            footer_style
        )
        elements.append(Spacer(1, 8))
        elements.append(footer)

        # Build the PDF
        doc.build(elements)
        return response

    except ConsultationReport.DoesNotExist:
        return HttpResponse("Report not found", status=404)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)




