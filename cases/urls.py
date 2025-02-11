from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CaseViewSet, CaseTypeViewSet

router = DefaultRouter()
router.register(r'cases', CaseViewSet)
router.register(r'casetypes', CaseTypeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
