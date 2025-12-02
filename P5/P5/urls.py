from django.contrib import admin
from django.urls import path
from ModelSerializer.views import *
from validation.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu-api/', StudentAPI.as_view()),
    path('stu-validate-api/', StudentValidateAPI.as_view()),
]
