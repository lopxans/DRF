from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from api.views import StudentModelViewSet

router = DefaultRouter()
router.register('students', StudentModelViewSet, basename='students')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
