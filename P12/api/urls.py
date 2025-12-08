from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from api.views import StudentViewset

router = DefaultRouter()
router.register('students', StudentViewset, basename='students')

urlpatterns = [
    path('', include(router.urls)),
]
