from django.urls import path
from .views import RegisterView, LoginView, UserDetailView,ConsultationView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='api-register'),
    path('login/', LoginView.as_view(), name='api-login'),
    path('user/', UserDetailView.as_view(), name='api-user'),
    path('consultation/', ConsultationView.as_view(), name='ai-consultation'),
]
