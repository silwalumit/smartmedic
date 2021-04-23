from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

# from rest_framework_simplejwt.tokens import Token
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        fields = (
            "username",   
            "password" 
        )

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        
        if username is None:
            raise serializers.ValidationError("Username is required to login!")

        if password is None:
            raise serializers.ValidationError("Password is required to login!")

        user = authenticate(username = username, password = password)

        if user is None:
            raise serializers.ValidationError("Invalid username or password")
            
        if not user.is_active:
            raise serializers.ValidationError("This user has been deactivated.")

        return data

class UserSerializer(serializers.ModelSerializer):
    c_password = serializers.CharField(
        label="Confirm Password",
        style={'input_type':'password'},
        write_only=True
    )

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "c_password"
        )

        extra_kwargs = {
            'password':{'write_only':True},
            'id':{'read_only':True},
            'email':{'read_only':True}
        }
    
    def validate_username(self, value):
        qs = User.objects.filter(username__iexact = value)

        if qs.exists():
            raise serializers.ValidationError("User with that email already exists")
        return value
    
    def validate(self, data):
        password = data.get('password')
        c_password = data.get('c_password')

        if password != c_password:
            raise serializers.ValidationError("Passwords must match")
        
        return data
    

    def create(self, validated_data):
        instance = User(username = validated_data.get("username"))
        instance.set_password(validated_data.get("password"))
        instance.save()
        
        return instance

