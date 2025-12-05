from django.urls import path
from .views import *

urlpatterns = [
    path('', student_api),
    path('<int:pk>/', student_api),
]
