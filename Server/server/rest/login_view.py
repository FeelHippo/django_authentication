from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import LoginSerializer

User = get_user_model()

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            # SELECT user from DB
            db_user = User.objects.get(
                email = user.email
            )
            is_password_valid = check_password(db_user.password, user.password)
            if is_password_valid == False:
                return Response(
                    { 'message': "error_wrong_password" },
                    status=status.HTTP_401_UNAUTHORIZED
                )
            token = Token.objects.create(user=db_user)
            return Response({ 'token': token.key, 'user': db_user })
        return Response(
                    { 'message': "error_invalid_data" },
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY
                )