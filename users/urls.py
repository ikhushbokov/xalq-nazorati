# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet
#
# router = DefaultRouter()
# router.register(r'users', UserViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
#
# ]

from django.urls import path, include
from .views import CustomUserViewSet
urlpatterns = [
    path('', CustomUserViewSet.as_view({'post': 'create'})),  # Custom user registration
]
