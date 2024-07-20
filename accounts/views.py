from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import AccountSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

class Signup(APIView):
     
     permission_classes = [AllowAny]

     def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            token, created = Token.objects.get_or_create(user=account)
            return Response(
                {
                    'message': "Account created successfully!",
                    'token': token.key
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)