from rest_framework import viewsets
from .models import Case, CaseTypes
from .serializers import CaseSerializer, CaseTypeSerializer
import requests
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404



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


def create_case_view(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard or another page after saving
    else:
        form = CaseForm()

    return render(request, 'create_case.html', {'form': form})


def list_cases_view(request):
    cases = Case.objects.all()  # Fetch all cases from the database
    return render(request, 'list_cases.html', {'cases': cases})


def update_case_view(request, case_id):
    case = get_object_or_404(Case, id=case_id)

    if request.method == 'POST':
        form = CaseForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard after saving
    else:
        form = CaseForm(instance=case)

    return render(request, 'update_case.html', {'form': form})


def delete_case_view(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    case.delete()  # Deletes the case
    return redirect('dashboard')  # Redirect back to the dashboard after deletion