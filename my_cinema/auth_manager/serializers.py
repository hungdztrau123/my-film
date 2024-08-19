
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from cinema_manager.models import UserProfile



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}}

class UserRegisterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=15, required=False)
    address = serializers.CharField(max_length=255, required=False)
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'phone', 'address',]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        phone = validated_data.pop('phone', None)
        address = validated_data.pop('address', None)
        
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(password)
        )
        UserProfile.objects.create(
            user=user,
            phone=phone,
            address=address,
        )
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user = instance.user
            user.username = user_data.get('username', user.username)
            # user.email = user_data.get('email', user.email)
            user.save()

        phone = validated_data.get('phone', instance.phone)
        address = validated_data.get('address', instance.address)
        instance.phone = phone
        instance.address = address
        instance.save()
        return instance
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'phone', 'address',]
        
class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['username', 'password']   

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')
       