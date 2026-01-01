from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from api.views import StudentModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register('students', StudentModelViewSet, basename='students')

urlpatterns = [
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('refreshtoken/', TokenRefreshView.as_view(), name="token_refresh"),
    path('varifytoken/', TokenVerifyView.as_view(), name="token_varify"),
]
