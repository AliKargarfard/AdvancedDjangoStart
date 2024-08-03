from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api-v1'

urlpatterns = [
    # registration
    path('registration/', views.RegistrationApiView.as_view(),name='registration'),
    path('token/signin', obtain_auth_token,name='token-signin'),

 ]