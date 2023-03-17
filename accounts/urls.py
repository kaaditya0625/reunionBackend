# from .views import RegisterAPI
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
     # path('api/login/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
     path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
     path('authenticate/', views.LoginAPIView.as_view(), name ='login_automate'),
     path('logout/', views.LogoutAPIView.as_view(), name ='login_automate'),
]