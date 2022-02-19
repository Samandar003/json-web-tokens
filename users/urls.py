from django.urls import path
from .views import hello
from .views import Register, LoginAPIView

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login')  
]


