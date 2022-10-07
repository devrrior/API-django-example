from apps.users.api.serializers import UserSerializer, UserValidateSerializer
from apps.users.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserValidate(APIView):
    def post(self, request):
        serializer = UserValidateSerializer(data=request.data)

        if serializer.is_valid():
            try:
                user = User.objects.get(email=serializer.data.get('email'))
            except ObjectDoesNotExist:
                user = None

            if user and user.password == serializer.data.get('password'):
                return Response({ 'message': 'User found' }, status=status.HTTP_200_OK)

            return Response({ 'message': 'Email or password is not correct' }, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
