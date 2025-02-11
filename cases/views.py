from rest_framework import viewsets
from .models import Case, CaseTypes
from .serializers import CaseSerializer, CaseTypeSerializer
from rest_framework.permissions import IsAuthenticated

class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = [IsAuthenticated]

class CaseTypeViewSet(viewsets.ModelViewSet):
    queryset = CaseTypes.objects.all()
    serializer_class = CaseTypeSerializer
    permission_classes = [IsAuthenticated]