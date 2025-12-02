from django.contrib import admin
from django.urls import path
from deserializer.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu-create/', student_create),
]
