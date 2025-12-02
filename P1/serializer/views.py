from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Model - Get Single data --------------------------------------
# def student_detail(request, id):
#     student = Student.objects.get(id=id)
#     serializer = StudentSerializer(student)
#     json_data = JSONRenderer().render(serializer.data)
    
#     return HttpResponse(json_data, content_type='application/json')

def student_detail(request, id):
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(student)
    
    return JsonResponse(serializer.data)

# Query Set - Get all data --------------------------------------
def student_list(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    
    return JsonResponse(serializer.data, safe=False)