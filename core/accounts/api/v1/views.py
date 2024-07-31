from rest_framework import generics, status
from .serializers import RegistrationSerializer
from rest_framework.response import Response

class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valied():
            serializer.save()
            data = {
                'email': serializer.validation_data['email']
            }
            return Response(data, status=status.HTTP_201_CREATED)

