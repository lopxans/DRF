from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# StudentLC View
# Handles:
#   - GET  : List all students
#   - POST : Create a new student
# No 'pk' required for this view

# class StudentLC(ListAPIView, CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

class StudentLC(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

# ---------------------------------------------------------
# StudentRUD View
# Handles:
#   - GET     : Retrieve a single student by ID
#   - PUT     : Update an existing student
#   - DELETE  : Remove a student from the database
# 'pk' is required for all actions in this view

# class StudentRUD(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer