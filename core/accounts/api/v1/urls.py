from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token, ObtainAuthToken

app_name = 'api-v1'

urlpatterns = [
    # registration
    path('registration/', views.RegistrationApiView.as_view(),name='registration'),
    path('token/login/', views.CustomAuthToken.as_view(),name='token-sign-in'),
    path('token/logout/', views.CustomDeleteAuthToken.as_view(),name='token-sign-out'),

 ]