from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentLC.as_view()),
    path('<int:pk>/', StudentRUD.as_view()),
]
