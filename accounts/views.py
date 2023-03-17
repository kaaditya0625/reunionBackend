from rest_framework import generics
from django.contrib.auth import authenticate,login,logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# follower
# user = onetoonefield(user
# followers = foreignkey(user))

# from django.db import models
# from django.contrib.auth.models import User

# class Follower(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='follower')

# class Follower(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='follower')
    
# class User(models.Model):
#     # ... other fields ...
#     followers = models.ForeignKey(Follower, on_delete=models.CASCADE, related_name='following')

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # request.user.auth_token.delete()
        logout(request)
        return Response({"success": "Successfully logged out."}, status=status.HTTP_200_OK)