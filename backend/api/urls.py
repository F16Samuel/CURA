from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='api-register'),
    path('login/', LoginView.as_view(), name='api-login'),
    path('user/', UserDetailView.as_view(), name='api-user'),
    # path('consultation/', ConsultationView.as_view(), name='ai-consultation'),
    # path('current-user/', get_user_data, name='current-user'),
    path("get_user/", get_user_data, name="get_user_data"),
    path("logout/", logout_view, name="logout"),
    path('api/save-consultation/', save_consultation, name='save-consultation'),
    path("api/generate-report/<int:report_id>/", generate_pdf, name="generate-pdf"),
    path("csrf/", csrf_token_view, name="csrf_token"), 
    path('api/diagnose-symptoms/', diagnose_symptoms, name='diagnose-symptoms'),

]