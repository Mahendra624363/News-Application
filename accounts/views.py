from django.shortcuts import render
from .serializers import RegisterSerializer,ProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated,AllowAny

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registration Successful"}, status=201)

        print("ERRORS:", serializer.errors)  # 🔥 IMPORTANT
        return Response(serializer.errors, status=400)
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        serializer=ProfileSerializer(request.user)
        return Response({'userinfo':serializer.data})

class LogoutView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        try:
            refresh_Token=request.data.get('refresh')
            if not refresh_Token:
                return Response({"message":"refresh token expired"})
            token=RefreshToken(refresh_Token)
            token.blacklist()
            return Response({"message":"Logout Successful"})
        except Exception as e:
            return Response({'error':'something went wrong'})