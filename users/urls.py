from django import views
from django.urls import path
# from .views import Register, LoginAPIView, UserView, LogoutView
from . import views

urlpatterns = [
    path('', views.hello, name='home'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
]

