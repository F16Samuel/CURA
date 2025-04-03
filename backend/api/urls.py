from django.urls import path
from .views import RegisterView, LoginView, UserDetailView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='api-register'),
    path('api/login/', LoginView.as_view(), name='api-login'),
    path('api/user/', UserDetailView.as_view(), name='api-user'),
]
