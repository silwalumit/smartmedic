from django.urls import path
from .views import UserCreateAPIView, AuthAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path("login/", AuthAPIView.as_view()),
    path("signup/", UserCreateAPIView.as_view()),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]