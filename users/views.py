from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from djoser.views import UserViewSet
from .serializers import CustomUserCreateSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomUserViewSet(UserViewSet):
        serializer_class = CustomUserCreateSerializer