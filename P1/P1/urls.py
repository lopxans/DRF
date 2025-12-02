from django.contrib import admin
from django.urls import path
from serializer.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_list),
    path('stu-info/<int:id>/', student_detail),
]
