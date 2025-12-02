from api.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu-api/', StudentAPI.as_view()),
]
