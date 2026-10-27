from django.shortcuts import render

from django.contrib.auth.models import User

from rest_framework import viewsets,status,generics
from rest_framework.decorators import action

from rest_framework.permissions import(


    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly
)
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .models import Job,Jobseeker
from .serializers import RegisterSerializer,JobSerializer,JobseekerSerializer


class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes=[AllowAny]

class LoginView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(

            username=username,
            password=password
        )
        if(user is None):
            return Response({'error':'invalid username or password'})
        
        token,created=Token.objects.get_or_create(user=user)
        return Response({'message':'login successfully','username':username,'token':token.key})

class JobViewSet(viewsets.ModelViewSet):
    serializer_class=JobSerializer
    permission_classes=[
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_query(self,request):
        queryset=Job.objects.filter(
            is_active=True
        ).select_related('posted_by')
        return queryset
    def create_query(self,serializer):
        serializer.save(posted_by=self.request.username)
    







