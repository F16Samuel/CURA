from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='api-register'),
    path('login/', LoginView.as_view(), name='api-login'),
    path('user/', UserDetailView.as_view(), name='api-user'),
    path('consultation/', ConsultationView.as_view(), name='ai-consultation'),
    # path('current-user/', get_user_data, name='current-user'),
    path("get_user/", get_user_data, name="get_user_data"),
    path("logout/", logout_view, name="logout"),

]
