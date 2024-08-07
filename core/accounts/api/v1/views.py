from rest_framework import generics, status
from .serializers import (
    RegistrationSerializer,
    CustomAuthTokenSerializer,
    CustomTokenOptainPairSerializer,
    ChangePasswordSerializer
)
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model

User=get_user_model


class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'email':serializer.validated_data['email']
                }
            print ('...................',data)
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class CustomDeleteAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomAuthTokenSerializer

class ChangePasswordView(generics.GenericAPIView):
    model = User
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self, queryset=None):
        obj = self.queryset.user
        return (obj)
        
    def put(self, request, *args, **kwargs):
        self.get_object = self.get_object()
        serializer = self.serializer(data = reuest.data)
        if serializer.is_valid():
            if not self.object.check_password(serializet.data.get('old_password')):
                return Response({'old_password':['wrong password']},status= status.HTTP_400_BAD_REQUEST)
                self.object.set_password(serializet.data.get('new_password'))
                self.object(save)
            return Response({'detail': 'password changed successfully'},status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)