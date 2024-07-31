from django.urls import path, include
from .views import RegistrationApiView

app_name = 'api-v1'

urlpatterns = [
    # registration
    path('register/', RegistrationApiView.as_view(),name='registration'),

 ]