from django.contrib import admin
from django.urls import path
from crud_CB.views import StudentAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentAPI.as_view()),
    path('<int:pk>/', StudentAPI.as_view()),
]
