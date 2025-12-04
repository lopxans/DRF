from django.urls import path
from .views import *

urlpatterns = [
    path('', student_list),
    path('<int:id>/', student_detail),
]
