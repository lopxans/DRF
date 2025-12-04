from django.urls import path
from .views import *

urlpatterns = [
    path('', LCStudentAPI.as_view()),
    path('<int:pk>/', RUDtudentAPI.as_view()),
    
]
