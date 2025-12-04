from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# List and Create - PK Not Required
class LCStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    # Get Data 
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    # Post Data
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Retrieve Update & Destroy - PK Required
class RUDtudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    # Retrieve Data: Get Singlevvv
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # Update Data
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # Delete Data
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)