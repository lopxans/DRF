from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# Get Data
class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



# Retrieve Data: Get Single data
class StudentRetrive(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# Create Data
class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Update Data
class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

# Delete Data
class StudentDelete(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)