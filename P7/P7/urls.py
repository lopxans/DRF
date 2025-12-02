from django.contrib import admin
from django.urls import path
from FBapi_view.views import *
from crud.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', hello_world),
    path('', student_api),
]
