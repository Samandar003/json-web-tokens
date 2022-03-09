from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from users.models import User
from .serializers import UserSerializer
from rest_framework.response import Response

def hello(request):
  return HttpResponse('It is me')

class Register(APIView):
  def post(self, request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  
class LoginView(APIView):
  def post(self, request):
    email = request.data['email']
    password = request.data['password']  
    user = User.objects.filter(email=email).first()
    if user is None:
      raise AuthenticationFailed('User note found')
    if not user.check_password(password):
      raise AuthenticationFailed('Incorrect password')
    return Response({
        "message":"success"
      })
    
