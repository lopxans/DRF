from django.contrib import admin
from django.urls import path, include
from generic.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentList.as_view()),
    path('<int:pk>/', StudentRetrive.as_view()),
    path('c/', StudentCreate.as_view()),
    path('u/<int:pk>', StudentUpdate.as_view()),
    path('d/<int:pk>', StudentDelete.as_view()),
    
    path('m/', include('mixins.urls')),
]
