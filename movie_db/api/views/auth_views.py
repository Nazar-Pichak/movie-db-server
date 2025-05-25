from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import RegisterSerializer, UserSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import login, logout, authenticate


class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AuthView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        """ Získání informací o přihlášeném uživateli """
        if not request.user.is_authenticated:
            return Response({'error': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({
            '_id': request.user.id,
            'email': request.user.email,
            'isAdmin': request.user.is_staff
        }, status=status.HTTP_200_OK)

    def post(self, request):
        """ Přihlášení uživatele """
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)

        return Response({
            '_id': user.id,
            'email': user.email,
            'isAdmin': user.is_staff
        }, status=status.HTTP_200_OK)
        
    def delete(self, request):
        """ Odhlášení uživatele """
        if request.user.is_authenticated:
            logout(request)
            return Response({'message': 'Uživatel odhlášen'}, status=status.HTTP_200_OK)
        return Response({'error': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)