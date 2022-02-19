from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import Student
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

def hello(request):
  return HttpResponse('Hello it is me')

class Register(APIView):
  def post(self, request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

class LoginAPIView(APIView):
  def post(request):
    email = request.data['email']
    password = request.data['password']

    user = User.objects.filter(email=email).first()
    if user is None:
      raise AuthenticationFailed('User not Found')
    if not user.check_password(password):
      raise AuthenticationFailed('Incorrect                                                                                                                                                                                                                                                                                                                                                               n ')
      
    
