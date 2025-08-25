from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            # INSERT user on db
            db_user = User.objects.create(
                email = user['email'],
                password = make_password(user['password']),
                first_name = user['first_name'],
                last_name = user['last_name'],
            )
            # generate new access token
            token = Token.objects.create(user=db_user)
            return Response({ 'token': token.key }, status=status.HTTP_200_OK)
        return Response(
                    { 'message': "error_invalid_data" },
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY
                )