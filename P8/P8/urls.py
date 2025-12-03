from django.contrib import admin
from django.urls import path
from crud_FB.views import student_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_api),
    path('<int:pk>/', student_api),
]
