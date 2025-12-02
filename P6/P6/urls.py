from django.contrib import admin
from django.urls import path
from validation.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu-validate-api/', StudentValidateAPI.as_view()),
]
