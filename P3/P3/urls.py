from django.contrib import admin
from django.urls import path
from crud_FBV.views import *
from crud_CBV.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-f/', student_api),
    path('api-c/', StudentAPI.as_view()),
]
