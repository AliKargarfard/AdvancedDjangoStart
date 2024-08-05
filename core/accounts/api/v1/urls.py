from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token, ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = 'api-v1'

urlpatterns = [
    # registration
    path('registration/', views.RegistrationApiView.as_view(),name='registration'),


    path('token/login/', views.CustomAuthToken.as_view(),name='token-sign-in'),
    path('token/logout/', views.CustomDeleteAuthToken.as_view(),name='token-sign-out'),

    path('jwt/create/', TokenObtainPairView.as_view(),name='jwt-create'), 
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),   
    path('jwt/verify/', TokenRefreshView.as_view(), name='jwt_verify'),

 ]