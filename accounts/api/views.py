from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model, login, authenticate
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import JSONParser

User = get_user_model()

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class AuthAPIView(APIView): 
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        
        data = request.data
        username = data.get("username", None)
        password = data.get("password", None)

        user = authenticate(username = username, password = password)
        
        if user:
            login(request, user)
            return Response(self.get_token(user), status=status.HTTP_200_OK)          
        
        return Response({"message":"Invalid username or password"}, status = status.HTTP_401_UNAUTHORIZED)

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            "user":UserSerializer(user).data,
            "refresh":str(refresh),  
            "token":str(refresh.access_token)
        }
