from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin,
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
)


# ---------------------------------------------------------
# StudentLC View
# Handles:
#   - GET  : List all students
#   - POST : Create a new student
# No 'pk' required for this view
# ---------------------------------------------------------
class StudentLC(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # Return list of all students
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    # Create a new student record
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# ---------------------------------------------------------
# StudentRUD View
# Handles:
#   - GET     : Retrieve a single student by ID
#   - PUT     : Update an existing student
#   - DELETE  : Remove a student from the database
# 'pk' is required for all actions in this view
# ---------------------------------------------------------
class StudentRUD(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # Retrieve a single student (GET /student/<pk>/)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    # Update a student (PUT /student/<pk>/)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    # Delete a student (DELETE /student/<pk>/)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
