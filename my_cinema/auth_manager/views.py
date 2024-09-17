from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from cinema_manager.permissions import  AccessTokenPermission,UserPermission, AdminPermission
from my_cinema.views import StandardPagination
from auth_manager.serializers import  UserSerializer, UserLoginSerializer, UserRegisterSerializer, LogoutSerializer, UserProfileSerializer
from auth_manager.filters import UserFilterSet, UserProfileFilterSet
from cinema_manager.models import UserProfile


class LogoutAPIView(APIView):
    serializer_class = LogoutSerializer
    permission_classes = [AccessTokenPermission]

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('logout!',status=status.HTTP_204_NO_CONTENT)


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Đăng ký thành công!',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error_messages': serializer.errors,
                'error_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self,request,format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('username')
        password = serializer.data.get('password')
        user = User.objects.get(email=email)
        if user is not None:
            if user.check_password(password) is False:
                return Response({'message: ':'Password not match','status':'400'}, status=status.HTTP_400_BAD_REQUEST)
            refresh = RefreshToken.for_user(user)
            if user.is_active is False: return Response({'message: ':'Account unable','status':'400'}, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            return Response({
                'errors':'user not found',
                'status':404
                }, 
                status=status.HTTP_404_NOT_FOUND)
    
        return Response({
            'status':200,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'name':user.username,
            'id':user.id,
            'is_admin': user.is_staff,
            'message':'Login Success'}, status=status.HTTP_200_OK)
        
        

    
class UserViewSet(ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardPagination
    permission_classes = [AdminPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = UserFilterSet
    ordering_fields = ("id", "email", "username",)
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    
class UserProfileViewSet(ModelViewSet):
    model = UserProfile
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    pagination_class = StandardPagination
    permission_classes = [AccessTokenPermission]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = UserProfileFilterSet
    ordering_fields = ("id", "phone")
    
    def get_permissions(self):
        return [permission() for permission in self.permission_classes]