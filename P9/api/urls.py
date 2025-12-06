from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentAPI.as_view()),
    path('<int:pk>/', StudentAPI.as_view()),
]
