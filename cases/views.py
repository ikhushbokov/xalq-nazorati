from rest_framework import viewsets
from .models import Case, CaseTypes
from .serializers import CaseSerializer, CaseTypeSerializer
import requests
from django.shortcuts import render

class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class CaseTypeViewSet(viewsets.ModelViewSet):
    queryset = CaseTypes.objects.all()
    serializer_class = CaseTypeSerializer



def dashboard_view(request):
    # Get Case data from the DRF API
    case_response = requests.get('http://127.0.0.1:8000/api/cases/')  # Adjust the API URL
    cases = case_response.json() if case_response.status_code == 200 else []

    # Get CaseType data from the DRF API
    case_type_response = requests.get('http://127.0.0.1:8000/api/casetypes/')  # Adjust the API URL
    case_types = case_type_response.json() if case_type_response.status_code == 200 else []

    # Pass the data to the template
    return render(request, "dashboard.html", {"cases": cases, "case_types": case_types})
